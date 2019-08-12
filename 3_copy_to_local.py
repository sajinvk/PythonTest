#!/root/anaconda3/bin/python
import os
import shutil 
import sys 
import subprocess 
import shlex 
import re
import datetime  
#Edit Variable if required
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
#
#source directories 
v_pronto = "/pro/pronto/"
v_lib = v_pronto + "lib/"
v_lbin = v_pronto + "lbin/"

def check_superuser (num):
	if num == 0:
		print ("All good - Continue") 
	else:
		print (" Run the script as a super user")
		sys.exit()

	
def rsync_directories_oldserver (sourcedir , destdir ):
	print ('Copying from ' + sourcedir  + ' to ' +  destdir    )        
	print (datetime.datetime.now() )        
	rsync_text = 'rsync -avh '+ sourcedir + '  ' + destdir         
	subprocess.call(shlex.split(rsync_text))
	print ( 'copy completed at: ')
	print (datetime.datetime.now() )
###################################################################
check_superuser(num = os.getuid())
rsync_directories_oldserver(dir_lbin,v_lbin )
