#!/usr/bin/python
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
destdir = "/usr/local/phs/bin"
dir_etc = dir_nondata +"etc/"
dir_lbin = dir_nondata +"lbin/"
dir_lib = dir_nondata +"lib/"
dir_cus = dir_nondata +"cus/"
collection = [ dir_main, dir_data , dir_nondata , destdir, dir_etc , dir_lbin, dir_lib, dir_cus]
dir_samba = dir_etc + "samba/"
f_passwd = dir_etc + "passwd"
f_shadow = dir_etc + "shadow"
f_new_passwd = "/etc/passwd"
pronto_admin = "psd"
admin_user_list = ["psd","pronto","appserv","informix","idsconx"]
#
ldap="-ldap"
home="-retainhome"
logfile="/root/golive/import_data.log"

def check_superuser (num):
	if num == 0:
		print "All good - Continue" 
	  	return ; 		
	else:
		print " Run the script as a super user"
		sys.exit()

def directory_structure():
	for name in collection:
		if not os.path.exists(name): 
			os.makedirs(name)
	return;
	
def copy_files (sourcename , filename, destdir):
	sourcefile=sourcename+filename
	if os.path.isfile(sourcefile) and os.path.isdir(destdir):
		shutil.copy2(sourcefile, destdir)
		return ; 
	else:
		print " Cannot copy file:" , filename			
		sys.exit()
	
def samba_setup():
		copy_files(dir_samba, "smb.conf","/etc/samba")
		if os.path.isfile("/oldserver/nondata/etc/samba/samba-users.backup"):
			subprocess.call(shlex.split('pdbedit -i smbpasswd:/oldserver/nondata/etc/samba/samba-users.backup'))
		else:
			print "export samba users from the source server and move the file to /oldserver/nondata/etc/samba/samba-users.backup "


###################################################################
#			# Main 
###################################################################
check_superuser(num = os.getuid())
directory_structure()
samba_setup()
#user_migrate()
