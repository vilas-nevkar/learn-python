"""
This module SSH to remote server and executes the commands
"""
import paramiko

server = ''
username = ''
password = ''

ssh = paramiko.SSHClient()
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
