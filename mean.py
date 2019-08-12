# coding: utf-8
# %load mean.py
# %load mean.py
# %load mean.py
import random
import math

vcounter=[random.randint(1,100) for x in range(15,20)]
print(vcounter)
def mean(x):
    return sum(x)/len(x)
print(mean(vcounter))

def deviation_mean(y):
    xmean=mean(vcounter)
    return [y_i-xmean for y_i in y]
#dmean = Deviation from mean 
def sum_of_squares():
    x_dmean=deviation_mean(vcounter)
    print(x_dmean)
    x_sqr_dmean = [x*x for x in x_dmean]
    print(x_sqr_dmean)
    return sum(x_sqr_dmean)
sum_of_squares()
def variance():
    v=sum_of_squares()
    var=v/(len(vcounter)-1)
    return var

print (variance())

    
def std_deviation():
        return math.sqrt(variance())
print (std_deviation())
   
