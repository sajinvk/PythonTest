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
	

def migrate_users_ldap (dir_nondata):
	copy_files (dir_nondata, "passwd" , destdir)
	copy_files (dir_nondata, "shadow", destdir)
	if os.path.isfile("/usr/local/phs/bin/creaccount.sh"):
		os.chdir("/usr/local/phs/bin/")
		with open ('/root/golive/ldap-users.sh', "w") as outfile: 
			subprocess.call(shlex.split('/usr/local/phs/bin/creaccount.sh -ldap -retainhome'),stdout=outfile)
	#		output=	subprocess.Popen(shlex.split('/usr/local/phs/bin/creaccount.sh -ldap -retainhome'), stdout=subprocess.PIPE)
		return;
	else:
		print " Issue is creating ldap scirpt" 

def move_files_to_lbin():
	if os.path.isdir("/oldserver/nondata/lbin") and os.path.isdir("/pro/pronto/lbin"):
		subprocess.call(shlex.split('rsync -avh /oldserver/nondata/lbin/ /pro/pronto/lbin/'))
		return ;
	else:
		print "Error copying lbin directory"	
		sys.exit()

def setupprinters():
	if os.path.isdir("/oldserver/nondata/lib"):
		subprocess.call(shlex.split('rsync -avh /oldserver/nondata/lib/*.env  /pro/pronto/lib/'))
		copy_files( "/oldserver/nondata/lib/" ,"printers","/pro/pronto/lib")
		copy_files( "/oldserver/nondata/lib/" ,"printcap","/pro/pronto/lib")
		copy_files( "/oldserver/nondata/etc/cups/" ,"printers.conf","/etc/cups/")
		subprocess.call(shlex.split('service cups restart'))
		return;
	else:
		print "Issue with setting up printers"

def samba_setup():
		print dir_samba
		copy_files(dir_samba, "smb.conf","/etc/samba")
		print dir_samba
		if os.path.isfile("/oldserver/nondata/etc/samba-users.backup"):
			subprocess.call(shlex.split('pdbedit -i smbpasswd:/oldserver/nondata/etc/samba-users.backup'))
		else:
			print "Error in Samba setup"

def copy_cus():	 
	if os.path.isdir("/oldserver/nondata/cus"):
		subprocess.call(shlex.split('rsync -avh /oldserver/nondata/cus/  /pro/pronto/cus/'))
		return ;
	else :
		print " Error copying CUS files"

def get_prontogid(f_name):
        #f_passwd = dir_etc + "passwd1"
        if os.path.isfile(f_name):
                with open(f_name, 'r') as infile:
                        for line in infile:
                                if line.split(":")[0] == pronto_admin:
                                        pronto_group_id = line.split(":")[3]
                                        return pronto_group_id
        else:
           print "Error reading password file from the old server"
           return "x"

def get_useridnum(f_name):
        with  open (f_new_passwd) as file1:
                lines = file1.readlines()
                last_row = lines[-1]
#               print last_row
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
                                                if line.split(":")[2] <  int(var1):
                                                        new_file.write( line.split(":")[0]+ ":" + line.split(":")[1]+ ":"+str(int( line.split(":")[2]) + 100)+pronto_newgroup_id+":"+line.split(":")[4]+ ":"+line.split(":")[5]+ ":"+line.split(":")[6]+"\n")
                                                else:
                                                        new_file.write(line.split(":")[0]+ ":" + line.split(":")[1]+ ":"+line.split(":")[2] +":" +pronto_newgroup_id+":"+line.split(":")[4]+ ":"+line.split(":")[5]+ ":"+line.split(":")[6]+"\n")
					array_user.append (line.split(":")[0])	
	else:
                print "Error Reading Pronto GID"
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
#migrate_users_ldap(dir_nondata)
#directory_structure()

#move_files_to_lbin()
#setupprinters()
#samba_setup()
#copy_cus()
user_migrate()
