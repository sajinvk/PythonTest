# coding: utf-8
# %load matlab_histogram.py
from matplotlib import pyplot as plt
from collections import Counter 
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: (grade // 10 ) * 10
histogram = [decile(grade) for grade in grades]
xs = [x*10 for x in range(10)]
histogram_count = Counter(histogram)
print (histogram_count)
plt.bar(histogram_count.keys() , histogram_count.values())
plt.show()
