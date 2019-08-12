# coding: utf-8
list1 = ["Michael Jackson" , 10.1,1982]
list1
list1[2:3]
list1[2:4]
list1.extend["pop", 10]
list1.extend(["pop", 10])
list1[2:4]
list1.append(["pop", 10])
list1
list1.append(("pop", 10))
list1
#lists are mutable 
A=["disco",10,1.2]
print('Before change:', A)
A[0] = "rock"
print('After change:', A)
delA[0]
del(A[0])
A
string= "A,B,C,D"
string.split(,)
string.split(",")
A = [1,2,3]
B= A
print(B)
A[0] = 0
print(B)
#fuck A is changed and the change is transfered to B
C=A[:] # clone of A 
print (C)
A[0] = 99
print (C)
# C is intact 
