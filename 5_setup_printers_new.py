#!/root/anaconda3/bin/python
import os
import shutil
import sys
import subprocess as sp
import shlex
import re
import datetime
import logging 
#Edit Variable if required
#check $PRONTO variable in oldserver
v_pronto="/pro/pronto/"
v_lbin=v_pronto+"lbin/"
v_lib=v_pronto+"lib/"

#
dir_main = "/oldserver"
dir_data = "/oldserver/data/"
dir_nondata = "/oldserver/nondata/"
dir_etc = dir_nondata +"etc/"
dir_cups = dir_etc+"cups/"
dir_lib = dir_nondata +"lib/"
#
def SetupLogging():
    try:
        debug = 0
        if debug == 1 :
           info = logging.DEBUG
        else :
           info = logging.INFO
        logger = logging.getLogger()
        logger.setLevel(info)
        #create a file handler
        handler = logging.FileHandler('/tmp/printers_mig.out')
        handler.setLevel(info)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
    except IOError:
        logger.error("cannot open log file",exc_info=True)

def UnixCmd(cmd):
    try:
        p_out = sp.Popen(shlex.split(cmd), stderr=sp.PIPE , stdout=sp.PIPE)
        out = p_out.communicate()
        return(out[0],out[1])
    except OSError as e:
        logging.info(e.errno , e.strerror )
    except:
        logging.info("error" , sys.exc_info())



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
                print (" Cannot copy file: " + filename)
                sys.exit()


def setupprinters():
        if os.path.isdir(dir_lib):
                copy_files( dir_lib ,"printers",v_lib)
                copy_files( dir_lib ,"printcap",v_lib)
                copy_files(dir_cups  ,"printers.conf","/etc/cups/")
                #subprocess.call(shlex.split('service cups restart'))
                out,error = UnixCmd("service cups restart")
                return;
        else:
                print ("Issue with setting up printers")

#Main
check_superuser(num = os.getuid())
setupprinters()

