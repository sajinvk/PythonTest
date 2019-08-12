# coding: utf-8
#list Comprehension
even_num = [ x in for i in range(10) if i % 2 == 0 ]
even_num = [ x  for i in range(10) if i % 2 == 0 ]
even_num = [ i  for i in range(10) if i % 2 == 0 ]
print (even_num)
square_list = [ i*i  for i in range(10)  ]
print (square_list)
square_dict = {i : i*i  for i in range(10)}
print (square_dict)
pairs = [(x,y) 
for x in range(5)
for y in range (5)]
print (pairs)
lazy_evens_below20 = [ x for x in lazy_range(20) if x % 2 == 0 ]
