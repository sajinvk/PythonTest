#!/root/anaconda3/bin/python
import sys 
print ( " This script creates a file hosts and network in the directory where the script is run from" ) 

etc_hosts = "/etc/hosts"
etc_network = "/etc/sysconfig/network"

def valid_ip4_addr(ipv4addr):
    parts = ipv4addr.split(".")
    if len(parts) != 4:
       return False
    for item in parts:
        if not 0 <= int(item)  <=255 :
            return False
    return True

def  write_host(prontoip,cogip , hostname,coghostname,bkpzpool_ip_addr):
         with open ("hosts","w") as file1:
              with open (etc_hosts,"r") as file2:
                  lines = file2.readlines()
                  for line in lines:
                       if "pronto" in line:
                           file1.write(line.replace(line,"#"+line))
                           file1.write(prontoip + " " + hostname + " " + hostname+".phs.local" + " " + "pronto")
                       elif "cognos" in line:
                           file1.write("\n" +line.replace(line,"#"+line))
                           file1.write(cogip + " " + coghostname + " " + coghostname+".phs.local" + " " + "cognos")
                       elif "backup.lan.phs.local" in line:
                           file1.write("\n" +line.replace(line,"#"+line))
                           file1.write(bkpzpool_ip_addr + " " +"backup.lan.phs.local")
                       else:
                           file1.write(line)
              file2.close()
         file1.close()

def write_network(hostname):
	with open ("network" ,"w" ) as file1:
		with open (etc_network,"r") as file2:
			lines = file2.readlines()
			for line in lines:
				if "HOSTNAME" in line:
                           		file1.write(line.replace(line,"#"+line))
                           		file1.write("HOSTNAME=" +  hostname+".phs.local" )
				else:
                           		file1.write(line)

def get_ip_address():
    pronto_ip_addr=input(" Enter Pronto IP address: ")
    if not valid_ip4_addr(pronto_ip_addr):
        print (" Invalid Pronto IP addresss ")	
        sys.exit()	
    cognos_ip_addr=input(" Enter Cognos  IP address: ")
    if not valid_ip4_addr(cognos_ip_addr):
        print (" Invalid Cognos  IP addresss ")	
        sys.exit()	
    bkpzpool_ip_addr=input(" Enter bkp_zpool  IP address: ")
    if not valid_ip4_addr(bkpzpool_ip_addr):
        print (" Invalid bkp zpool IP addresss ")	
        sys.exit()	
    pronto_server_name=input(" Enter Pronto local server name (Do not suffix phs.local): ")
    cognos_server_name=input(" Enter Cognos local server name (Do not suffix phs.local): ")
    write_host(pronto_ip_addr,cognos_ip_addr, pronto_server_name , cognos_server_name,bkpzpool_ip_addr)
    write_network(pronto_server_name)
#Main  
	
get_ip_address()

