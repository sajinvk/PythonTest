#!/root/anaconda3/bin/ipython
# Environment settings for Database 
import os 
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
    os.environ
    print(os.environ)
import IfxPy
conStr = "SERVER=pronto_net;DATABASE=sysmaster;HOST=pronto;SERVICE=9088;UID=informix;PWD=pronto1$;"
conn = IfxPy.connect( conStr, "", "")
sql = "select fname from syschunks"
stmt = IfxPy.exec_immediate(conn, sql)
dictionary = IfxPy.fetch_both(stmt)
while dictionary != False:
    print(dictionary[0])
    dictionary = IfxPy.fetch_both(stmt)
IfxPy.close(conn)
