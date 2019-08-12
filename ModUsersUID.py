Source_File="/oldserver/nondata/etc/passwd"
Dest_File="/oldserver/nondata/etc/passwd_new"
v_split =":"
def UserIDMod(Source_File):
    try:
        with open(Source_File,'r') as fh:
            for line in fh:
                var0=line.split(":")[0]
                var1=line.split(":")[1]
                var2=int(line.split(":")[2])+1000
                var3=line.split(":")[3]
                var4=line.split(":")[4]
                var5=line.split(":")[5]
                var6=line.split(":")[6]
                 
                #print (int(line.split(":")[2])+1000)
                with open( Dest_File, 'a') as new_fh:
                    new_fh.write(str(var0)+v_split+str(var1)+v_split+str(var2)+v_split+var3+v_split+var4+v_split+var5+v_split+var6)
    except OSError as err:
        print (err.errno , err.strerror )
        
        

UserIDMod(Source_File)
