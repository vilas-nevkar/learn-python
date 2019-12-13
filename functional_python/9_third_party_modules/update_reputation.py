#!/usr/bin/env python

# Reputation database downloader and updater
#
# vrt@alienvault.com
# aortega@alienvault.com

import os
import sys
import pycurl
import StringIO
import time
import re
import MySQLdb
import ConfigParser

sys.path.append("/usr/share/alienvault-center/av-libs/avconfig")
from utils import get_is_professional

global rep_serv
rep_serv = "https://reputation.alienvault.com/"

rep_file = "/etc/ossim/server/reputation.data"
rep_rev = "/etc/ossim/server/reputation.rev"

global log_file
log_file = "/var/log/ossim/reputation.log"

global curlrc
curlrc = "/etc/curlrc"

global lockfile
lockfile = "/tmp/.reputation_updater.lock"

global config_file
config_file = "/etc/ossim/ossim_setup.conf"

global db_encryption_file
db_encryption_file = "/etc/ossim/framework/db_encryption_key"

def lock():
	f = open(lockfile, "w")
	f.close()

def unlock():
	if os.path.exists(lockfile):
		os.unlink(lockfile)

def exit_proc(unlock_file = True):
	if unlock_file == True:
		unlock()
	sys.exit(0)

def write_repu_log(msg):
	try:
		f = open(log_file, "a")
		f.write("%s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg))
		f.close()
	except:
		pass

def read_curl_config():
	proxy = None
	if os.path.exists(curlrc) == True:
		r = re.compile("^proxy.*=(.*)$")
		f = open(curlrc, "r")
		data = f.read()
		f.close()
		for ln in data.split("\n"):
			m = r.match(ln)
			if m:
				proxy = m.group(1).replace(" ", "")
				break
	return proxy

def check_reputation_format(data):
	r = re.compile("^[+-]?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}#\d\d?#\d\d?#.*#.*#.*#.*#.*$")
	for ln in data.split("\n"):
		if ln != "":
			if not r.match(ln):
				return False
	return True

def get_db_info():
	# DB access information
	c = ConfigParser.ConfigParser()

	fix = False
	try:
		c.read(config_file)
	except:
		# Fix
		dummy = "[ossim]\n"
		f = open(config_file, "r")
		data = f.read()
		f.close()
		f = open("/tmp/.crafted_conf", "w")
		f.write("%s%s" % (dummy, data))
		f.close()
		c.read("/tmp/.crafted_conf")
		fix = True

	user = c.get('database','user')
	password = c.get('database','pass')
	host = c.get('database','db_ip')

	if fix == True:
		os.remove("/tmp/.crafted_conf")

	# DB encryption information
	c = ConfigParser.ConfigParser()
	c.read(db_encryption_file)
	db_encryption_key = c.get('key-value','key')

	return user, password, host, db_encryption_key

def get_db_cursor():
	try:
		dbUser, dbPass, dbHost, db_encryption_key = get_db_info()
	except:
		write_repu_log("Error-feedback: Unable to read database configuration")
		exit_proc()
	try:
		db=MySQLdb.connect(host=dbHost, user=dbUser, passwd=dbPass)
		cursor=db.cursor()
		return cursor, db_encryption_key
	except:
		write_repu_log("Error-feedback: Unable to connect to database")
		exit_proc()

def check_permisions(cursor, enc_key):
	global rep_serv
	if get_is_professional():
		rep_serv= "https://reputation.alienvault.com/USM/"
		return True
	else:
		clid = None
		sql = "select AES_DECRYPT(value, '"+enc_key+"') from alienvault.config where conf = 'open_threat_exchange_key';"
		cursor.execute(sql)
		data = cursor.fetchall()
		for i in data:
			clid = i[0]
		if clid:
			if clid and re.search("\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", clid) or re.search("[0-9a-fA-F]{64}", clid):
				rep_serv = "https://reputation.alienvault.com/%s/" %(clid)
				return True
	return False

def get_url(url):
	try:
		proxy = read_curl_config()
		buffer = StringIO.StringIO()
		c = pycurl.Curl()
		c.setopt(pycurl.URL, url)
		c.setopt(pycurl.SSL_VERIFYPEER, 0)
		c.setopt(pycurl.WRITEFUNCTION, buffer.write)
		if proxy:
			c.setopt(pycurl.PROXY, proxy)
		c.perform()
		rcode = c.getinfo(pycurl.HTTP_CODE)
		data = buffer.getvalue()
		c.close()
		if rcode != 200:
			return None
		else:
			return data
	except:
		return None

def get_remote_rep_rev(rep_serv):
	data = get_url("%sreputation.rev" % rep_serv)
	if data:
		return data.rstrip()
	else:
		return None

def get_remote_patch(rep_serv, revision):
	patch = get_url("%srevisions/reputation.data_%s" % (rep_serv, revision))
	return patch

def get_local_rep_rev(rep_rev):
	f = open(rep_rev, "r")
	data = f.read()
	data = data.rstrip()
	return data

def update_reputation_from_patch(rep_file, rep_rev, patch, remote_rev):
	f = open(rep_file, "r")
	rep_data = f.read()
	f.close()

	rep_data = rep_data.split("\n")
	patch_data = frozenset(patch.split("\n"))

	for i in patch_data:
		try:
			if i != "":
				if i[0] == "-":
					line = list(i) # Delete first char
					line[0] = ""
					line = "".join(line)
					rep_data.remove(line)
				elif i[0] == "+":
					line = list(i) # Delete first char
					line[0] = ""
					line = "".join(line)
					rep_data.append(line)
		except:
			pass

	# Dump new reputation
	f = open(rep_file, "w")
	for ln in rep_data:
		if ln != "":
			f.write("%s\n" % ln)
	f.close()

	# Dump new revision
	f = open(rep_rev, "w")
	f.write(remote_rev)
	f.close()

def download_reputation_database(rep_file, rep_rev, rep_serv):
	try:
		data = get_url("%sreputation.data" % rep_serv)
		if data != None:
			if check_reputation_format(data) == True:
				f = open(rep_file, "w")
				f.write(data)
				f.close()
		data = get_url("%sreputation.rev" % rep_serv)
		if data != None:
			f = open(rep_rev, "w")
			f.write(data)
			f.close()
	except:
		# Error downloading database from server
		write_repu_log("Error-update: Error downloading database from server")
		pass

# init
if os.path.exists(lockfile):
	# Process running, die now
	exit_proc(False)

lock()

dbcursor, enc_key = get_db_cursor()
if not check_permisions(dbcursor, enc_key):
	write_repu_log("Message-update: User not allowed to update reputation")
	exit_proc()

write_repu_log("Message-update: Running reputation updater")

if ((os.path.exists(rep_file) == False) or (os.path.exists(rep_rev) == False)):
	# No reputation file in this box, downloading it.
	write_repu_log("Message-update: Downloading reputation database for the first time")
	download_reputation_database(rep_file, rep_rev, rep_serv)
	write_repu_log("Message-update: Reputation database downloaded")
	exit_proc() # Done

# Check for updates
remote_rev = get_remote_rep_rev(rep_serv)
local_rev = get_local_rep_rev(rep_rev)

if remote_rev != local_rev:
	# Updating
	write_repu_log("Message-update: Updating database from server")
	patch = get_remote_patch(rep_serv, local_rev)
	if patch != None and remote_rev != None: # Updating your revision
		if check_reputation_format(patch) == True:
			update_reputation_from_patch(rep_file, rep_rev, patch, remote_rev)
	else: # No patch for your revision, downloading the complete database
		download_reputation_database(rep_file, rep_rev, rep_serv)

write_repu_log("Message-update: Reputation updated")
exit_proc()
