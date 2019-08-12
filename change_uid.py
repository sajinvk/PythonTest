#!/root/anaconda3/bin/ipython
##!/usr/bin/python
import os
import shutil 
import sys 
import subprocess 
import shlex 
import re 
#Edit Variable if required
dir_main = "/oldserver"
dir_data = "/oldserver/data/"
dir_nondata = "/oldserver/nondata/"
dir_etc = "etc/"
f_passwd = dir_etc + "passwd"
f_shadow = dir_etc + "shadow"
f_new_passwd = "/etc/passwd"
pronto_admin = "psd"
admin_user_list = ["psd","pronto","appserv","informix","idsconx"]
destdir = "/usr/local/phs/bin"
####
ldap="-ldap"
home="-retainhome"
logfile="/root/golive/import_data.log"

def check_superuser (num):
	if num == 0:
		print ("All good - Continue") 
	else:
		print (" Run the script as a super user")
		sys.exit()

	

def copy_files (sourcename , filename, destdir):
        sourcefile=sourcename+filename
        if os.path.isfile(sourcefile) and os.path.isdir(destdir):
                shutil.copy2(sourcefile, destdir)
                return ;
        else:
                print (" Cannot copy file:" , filename)
                sys.exit()

def migrate_users_ldap (dir_nondata):
	copy_files (dir_etc, "passwd" , destdir)
	copy_files (dir_etc, "shadow", destdir)
	if os.path.isfile("/usr/local/phs/bin/creaccount.sh"):
		os.chdir("/usr/local/phs/bin/")
		with open ('/root/golive/ldap-users.sh', "w") as outfile: 
			subprocess.call(shlex.split('/usr/local/phs/bin/creaccount.sh -ldap -retainhome'),stdout=outfile)
	#		output=	subprocess.Popen(shlex.split('/usr/local/phs/bin/creaccount.sh -ldap -retainhome'), stdout=subprocess.PIPE)
	else:
		print (" Issue is creating ldap scirpt") 


def get_prontogid(f_name):
        #f_passwd = dir_etc + "passwd1"
        if os.path.isfile(f_name):
                with open(f_name, 'r') as infile:
                        for line in infile:
                                if line.split(":")[0] == pronto_admin:
                                        pronto_group_id = line.split(":")[3]
                                        return pronto_group_id
        else:
           print ("Error reading password file from the old server")
           return "x"

def get_useridnum(f_name):
        with  open (f_new_passwd) as file1:
                lines = file1.readlines()
                last_row = lines[-1]
                return last_row.split(":")[2]

def user_migrate():
	array_user = []
	array_shadow = []
	pronto_group_id = get_prontogid(f_passwd)
	pronto_newgroup_id = get_prontogid(f_new_passwd)
        #print pronto_newgroup_id
	if pronto_group_id != "x":
		with open(f_passwd, 'r') as infile:
			lines = infile.read().splitlines()
			for line in lines:
				if line.split(":")[3] == pronto_group_id and line.split(":")[0] not in admin_user_list:
					with open (f_new_passwd) as file1:
						var1 = get_useridnum(f_new_passwd)
					with open ("passwd_appended", 'a') as new_file:
						if int(line.split(":")[2]) <  int(1000):
							new_file.write( line.split(":")[0]+ ":" + line.split(":")[1]+ ":"+str(int( line.split(":")[2]) + 100)+pronto_newgroup_id+":"+line.split(":")[4]+ ":"+line.split(":")[5]+ ":"+line.split(":")[6]+"\n")
						else:
							new_file.write(line.split(":")[0]+ ":" + line.split(":")[1]+ ":"+line.split(":")[2] +":" +pronto_newgroup_id+":"+line.split(":")[4]+ ":"+line.split(":")[5]+ ":"+line.split(":")[6]+"\n")
					array_user.append (line.split(":")[0])	
	else:
		print ("Error Reading Pronto GID")
#	print array_user
	with open(f_shadow, 'r') as infile:
		lines = infile.read().splitlines()
		for line in lines:
			for item in array_user:
				if item in line:  	
#					print line 
					with open ("shadow_file",'a') as new_file2:
						new_file2.write(line+"\n")	
###################################################################
#			# Main 
###################################################################
check_superuser(num = os.getuid())
var1= input ( "Is the server Hosted(Y) or not (N)")
if (var1 == 'y' or var1 == "Y"):
	#migrate_users_ldap(dir_nondata)
	print ("Use DBono script")
elif(var1 == 'n' or var1 == 'n'):
	user_migrate()
else:
	print ("Not valid - Type Y(Hosted) or N (On - Premise)")
