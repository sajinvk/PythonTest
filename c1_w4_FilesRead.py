# coding: utf-8
example1 = "/root/golive/python/ipython/basic_scripts/example1.txt"
file1 = open(example1,"r")
file1.name
file1.mode
filecontent = file1.read()
print (filecontent)
type(filecontent)
file1.close()
file1
#Better way of handling files 
whith open(example1 , 'r')
whith open(example1 , 'r') as file1:
with open(example1 , 'r') as file1:
    FileContent=file1.read()
    print(filecontent)
    
file1.closed
print(filecontent)
with open(example1 , 'r') as file1:
    FileContent=file1.readlines()
    print(filecontent)
    
with open(example1,"r") as file1:
        print(file1.read(16))
            print(file1.read(5))
with open(example1,"r") as file1:
        print(file1.read(16))
        print(file1.read(5))
        print(file1.read(9))
        
with open(example1 , 'r') as file1:
    FileContent=file1.readlines()
    print(FileContent)
    
    
with open(example1 , 'r') as file1:
    FileContent=file1.readlines()
    print(FileContent)
    
    
with open(example1,"r") as file1:
    print("first line: " + file1.readline())
    
with open(example1,"r") as file1:
           i=0;
                  for line in file1:
with open(example1 , 'r') as file1:
    i = 0 
    for line in file1:
        print ("iteration" , i , line)
         
with open(example1 , 'r') as file1:
    i = 0 
    for line in file1:
        print ("iteration" , i , line)
        i = i+1
         
with open(example1,"r") as file1:
        FileasList=file1.readlines()
        
FileasList()
FileasList[1]
for n in range(0,2):
    print(file1.readline())
    
with open(example1, 'r') as file1:
    for n in range(0,2)
with open(example1, 'r') as file1:
    for n in range(0,2):
        print(file1.readline())
        
