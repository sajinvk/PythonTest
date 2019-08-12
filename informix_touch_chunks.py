#!/root/anaconda3/bin/ipython
import os
import sys
import logging 
import subprocess as sp
import shlex
#Source file = "/oldsrv/informix_chunks.out"
#Log File : /tmp/informix_touch_files.out
print("Source file =/oldsrv/informix_chunks.out")
print ("Log File : /tmp/informix_touch_files.out")
f_read = "/oldsrv/informix_chunks.out"

# Requires environment variables to be set Before imports IFXPY module 
try:
    informix_dir=os.environ['INFORMIXDIR']
except KeyError:
    print ( "INFORMIX PATH is not setup - Exit ")
    os.exit()

#setup Logging
#try:
#    logging.basicConfig( filename = "/tmp/touch_chunks.out",
#                     filemode = "w",
                     #level = logging.INFO,
#                     level = logging.DEBUG,
                     #format = '%(asctime)s - %(name)s - %(levelname)s  — %(funcName)s:%(lineno)d - %(message)s',
#                     format = '%(message)s',
    # )
#except IOError:
#    logging.error("Cannot open log file",  exc_info=True) 
# end Logging 
def CheckUser():
    try:
        uid = os.geteuid()
        if uid == 0 :
            logging.info(" Logged in as root - Continue ") 
        else:
            logging.info("No privileges to run. Log in as user - 'root' ")
    except IOError:
        logging.info(" Couldn't get the uid")
                
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
        handler = logging.FileHandler('/tmp/informix_touch_files.out')
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

def ReadFile(f_name):
    try:
        with open(f_name, 'r') as f_handler:
            for line in f_handler:
                dirname = line.rsplit("/",1)[0]
                filename = line.rsplit("/",1)[1]
                if not os.path.exists(dirname):
                    out,err = UnixCmd("mkdir " + dirname)
                    out,err = UnixCmd("chown informix:informix  " +dirname)
                    out,err = UnixCmd("chmod 770  " +dirname)
                    logging.info(" Create Directory - Success " + dirname)
                else:
                    logging.info("Directory already exists " + dirname)
                print (line)
                if not os.path.isfile(line.strip()):
                    out,err = UnixCmd("touch " +line)
                    out,err = UnixCmd("chown informix:informix  " +line)
                    out,err = UnixCmd("chmod 660  " +line)
                    logging.info(" Create file - Success " + line )
                else:
                    logging.info(" File arleady exists " + line)                  
                    
    except OSError as e:
        logging.info(e.errno , e.strerror )
    except:
        logging.info("error" , sys.exc_info())
CheckUser()
#GetInformixVersion()
SetupLogging()
ReadFile(f_read)

print("Source file =/oldsrv/informix_chunks.out")
print ("Log File : /tmp/informix_touch_files.out")
