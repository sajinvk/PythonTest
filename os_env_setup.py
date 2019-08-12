# coding: utf-8
# %load os_environement_setup.py
import os, sys 
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
        print ('Failed re-exec:')
        

# import yourmodule
print (os.environ['LD_LIBRARY_PATH'])
