# coding: utf-8
def f_median(x)
def f_median(x):
    n_len=len(x)
    sorted_x=sorted(x)
    if n_len%2 == 1:
        midpoint = round(n_len/2 + 1)
        return sorted_x[midpoint]
    else:
        l_midpoint = round(n_len/2)
        r_midpoint = round(n_len/2+1)
        return ((sorted_x[l_midpoint] + sorted_x[r_midpoint])/2)
    
        
list1=[3 ,88, 5 ,7, 9 , 66 ] 
r= f_median(list1)
print (r)
list1=[3 ,88, 5 ,7, 9 , 66 ,5] 
r= f_median(list1)
print (r)
