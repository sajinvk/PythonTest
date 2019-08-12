# coding: utf-8
#RANDOM funtion
get_ipython().run_line_magic('clear', '')
import random
random_num_list = [ random.random() for x in range (4)]
print (random_num_list)
random_num = random.randrange(3)
print (random_num)
random_num = random.randrange(999)
print (random_num)
random_num = random.randrange(5,7)
print (random_num)
