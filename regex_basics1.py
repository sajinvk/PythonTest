# coding: utf-8
import re
def return_digits(string):
    pattern = r'\d{1,}'
    result = re.match(pattern , '007 is bond')
    return result.group()
def return_digits(string):
    pattern = r'\d{1,}'
    result = re.match(pattern , string)
    return result.group()
return_digits('007 is the bond')
return_digits('7 is the bond')
return_digits('7dsafaf is the bond')
