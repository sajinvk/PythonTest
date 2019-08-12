# coding: utf-8
# %load c1_w3_loops.py
squares = ["red" , "yelow" , "orange" ,"red"]
for i,s in enumerate(squares):
    print (i ,s)
    
for i in enumerate(squares):
    print (i)
    
    
for i in squares:
    print (i)
    
    
    
sq = ["red" , "yellow" ,"yellow", "orange" ,"red"]
new_sq=[]
i=0
while (sq[i]== "yellow"):
    new_sq.append(sq[i])
    i=i+1
    print (new_sq)
    
    
    
    
