#!/root/anaconda3/bin/ipython3
import os
import shutil 
import sys 
import shlex 
import re
import datetime  
#Edit Variable if required
#old server details -- user should be setup to login without password  
v_oldserver = "oldsrv"
v_user = "root" 
#check $PRONTO variable in oldserver 
v_pronto="/pro/pronto/"
v_lbin=v_pronto+"lbin/"
v_lib=v_pronto+"lib/"
v_cus=v_pronto+"cus/"
v_bms=v_pronto+"bms/"

#
dir_main = "/oldserver"
dir_data = "/oldserver/data/"
dir_nondata = "/oldserver/nondata/"
destdir = "/usr/local/phs/bin"
dir_etc = dir_nondata +"etc/"
dir_lbin = dir_nondata +"lbin/"
dir_lib = dir_nondata +"lib/"
dir_cus = dir_nondata +"cus/"
dir_bms = dir_nondata +"bms/"
collection = [ dir_main, dir_data , dir_nondata , destdir, dir_etc , dir_lbin, dir_lib, dir_cus,dir_bms]
dir_samba = dir_etc + "samba/"
f_passwd = dir_etc + "passwd"
f_shadow = dir_etc + "shadow"
f_new_passwd = "/etc/passwd"
#

def check_superuser (num):
	if num == 0:
		print ("All good - Continue") 
	else:
		print (" Run the script as a super user")
		sys.exit()

def directory_structure():
	for name in collection:
		if not os.path.exists(name): 
			os.makedirs(name)
	return;
	
def rsync_directories_oldserver (sourcedir , destdir , server = v_oldserver , user = v_user):
	print ('Copying from ' + sourcedir  + ' to ' +  destdir    )        
	print (datetime.datetime.now() )        
	rsync_text = 'rsync -avh '+ user + '@' + server + ':' + sourcedir + '  ' + destdir         
	subprocess.call(shlex.split(rsync_text))
	print ( 'copy completed at: ')
	print (datetime.datetime.now() )
###################################################################
check_superuser(num = os.getuid())
directory_structure()
#rsync_directories_oldserver("/etc/" , dir_etc)
#rsync_directories_oldserver(v_lbin , dir_lbin)
#rsync_directories_oldserver(v_lib , dir_lib)
#rsync_directories_oldserver(v_cus , dir_cus)
#rsync_directories_oldserver(v_bms , dir_bms)
