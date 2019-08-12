# coding: utf-8
#http://evc-cit.info/comsc020/python-regex-tutorial/
#https://regex101.com/r/cO8lqs/11
import re
result = re.match(r'AV' , 'AV Analytics test AV')
print (result)
print (result.group())
result = re.match(r'test' , 'AV Analytics test AV')
print (result.group())
print (result)
#Match has to the start of the string 
result = re.match(r'AV' , 'AV Analytics test AV')
print (result.start())
print (result.end())
#search : No restriction on the start of the string 
re.search(r'test','AV Analytics test AV')
result = re.search(r'test','AV Analytics test AV')
print(result.group())

pattern = re.compile(r'\w') # Print only the first charecter and not the whole word 
str1 = 'regex is awsome'
result = re.match(pattern, str1)
print (result.group())
pattern = re.compile(r'\w+')
result = re.match(pattern, str1)
print (result.group())
