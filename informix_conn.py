#!/root/anaconda3/bin/python
##!/usr/bin/python
import os
import shutil 
import sys 
import subprocess 
import shlex 
import re
import time
from subprocess import Popen, PIPE 
#Edit Variable if required
informix_uid = 500
#sql_cmd = "select * from system_companies "
sql_cmd = "select count(distinct (comp_code)) from parallel_procedures where parp_status <>3" 
db_name = "sysinfo"
sqlfile = "/tmp/informix.sql"

def check_superuser (num):
	if num == 0:
		print ("All good - Continue") 
	else:
		print (" Run the script as a super user")
		sys.exit()
#subprocess.call(shlex.split('/usr/local/phs/bin/creaccount.sh -ldap -retainhome'),stdout=outfile)

def db_connect(db_name,sql_cmd):
	n_process = []
	os.setuid(informix_uid)
	command1=  'dbaccess ' + db_name + ' ' +sqlfile   
	command1= ` echo "output to pipe \"awk '/[0-z]/'\" with out headings select count(distinct (comp_code)) from parallel_procedures where parp_status <> 3" | dbaccess sysinfo 2>/dev/null`   
	#subprocess.call(shlex.split(command1))
	n_process = subprocess.getoutput(command1)
	print (n_process)
###################################################################
#			# Main 
###################################################################
check_superuser(num = os.getuid())

with  open(sqlfile , 'w') as file2:
	TS = time.strftime('%a %H:%M:%S')
	file2.write(sql_cmd)

db_connect(db_name, sql_cmd)
