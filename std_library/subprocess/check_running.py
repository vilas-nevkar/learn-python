import subprocess
out = subprocess.getoutput("ps -ef | grep chrome")
print(out)
