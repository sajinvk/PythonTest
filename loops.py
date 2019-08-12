# coding: utf-8
get_ipython().run_line_magic('clear', '')
#print control flow statements 
a = 1
b = 2
if a > b:
    print (" you wish")
elif a > 3:
    print ( "2nd condition")
else:
    print (" All conditions fail")
    
#while loop 
x = 3
while i < x :
    print (i)
    i=i+ 1
    
while x < 10 :
    print (x)
    x=x    + 1
    
    
for i in range(10):
    print i 
for i in range(10):
    print (i)
     
for i in range(10):
    if i == 3:
        continue 
    elif i == 6:
        break 
    else:
        print (i)

for i, item in enumerate(L):
    # ... compute some result based on item ...
    L[i] = result        
