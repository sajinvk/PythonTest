# coding: utf-8
import shlex
from subprocess import Popen
import sys
def UnixCmd(cmd):
    try:
        p_out = Popen(shlex.split(cmd), stderr=PIPE , stdin=PIPE , stdout=PIPE)
        out, err = p_out.communicate()
        return ( out)
    except OSError as e:
        print (e.errno , e.strerror )
    except:
        print ("error" , sys.exc_info()[0])
        
a = UnixCmd("ls -l")
print(a)       
