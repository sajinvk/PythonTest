#!/root/anaconda3/bin/ipython
import os
import sys
import logging 
import subprocess as sp
import shlex
# Requires environment variables to be set Before imports IFXPY module 
try:
    informix_dir=os.environ['INFORMIXDIR']
except KeyError:
    print ( "INFORMIX PATH is not setup - Exit ")
    os.exit()

try:
    ld_lib_path=os.environ['LD_LIBRARY_PATH']
    LD_LIBRARY_PATH=informix_dir+"/lib:"+informix_dir+"/lib/esql:"+informix_dir+"/lib/cli:"+ld_lib_path
    os.environ['LD_LIBRARY_PATH']=LD_LIBRARY_PATH
except KeyError:
    print ( "No environment set for LD_LIBRARY_PATH")
    LD_LIBRARY_PATH=informix_dir+"/lib:"+informix_dir+"/lib/esql:"+informix_dir+"/lib/cli"
    os.environ['LD_LIBRARY_PATH']=LD_LIBRARY_PATH
    try:
        os.execv(sys.argv[0], sys.argv)
    except Exception:
        print ('Failed to setup environment variable  ')

import IfxPy 
#setup Logging
try:
    logging.basicConfig( filename = "/tmp/touch_chunks.sh",
                     filemode = "w",
                     #level = logging.INFO,
                     level = logging.DEBUG,
                     #format = '%(asctime)s - %(name)s - %(levelname)s  — %(funcName)s:%(lineno)d - %(message)s',
                     format = '%(message)s',
     )
except IOError:
    logging.error("Cannot open log file",  exc_info=True) 
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
        handler = logging.FileHandler('/tmp/informix_locks.out')
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

def SetProfile():
    cmd = "sh /etc/profile"
    ret_code = UnixCmd(cmd)	

def GetInformixVersion():
    logging.info("************* Start  DB Version ***************")
    out,error = UnixCmd("onstat -") 
    if out:
        logging.info(out.decode())
    else:
        logging.info(error.decode())   
    logging.info("************* End  DB Version ***************")

def DBConnect(sql):
    constr = "SERVER=pronto_net;DATABASE=sysmaster;HOST=pronto;SERVICE=9088;UID=informix;PWD=pronto1$;"
    conn = IfxPy.connect( constr, "", "")
    stmt = IfxPy.exec_immediate(conn, sql)
    dictionary = IfxPy.fetch_both(stmt)
    while dictionary != False:
        logging.info("touch " + dictionary[0]) 
        logging.info("chown informix:informix" + dictionary[0]) 
        logging.info("chmod 660 "  + dictionary[0]) 
        dictionary = IfxPy.fetch_both(stmt)
    IfxPy.close(conn)

CheckUser()
SetProfile()
#GetInformixVersion()
#Get List of chunks 
SQL1="select fname from syschunks"
DBConnect(SQL1)
