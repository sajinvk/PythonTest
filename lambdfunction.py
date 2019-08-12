#!/root/anaconda3/bin/python
print(" Lambda is a name less funtion used along with filer() and map()")
double = lambda x:x*2 
print (double(5))
my_list = [ 1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10 ]
my_even_list = list(filter(lambda x: (x%2 == 0),my_list))
print(my_even_list)
list1 = [2, 3, 4]
list2 = list(map(lambda x : (x*x) , list1))
print (list2)
