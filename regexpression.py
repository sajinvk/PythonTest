# coding: utf-8
#A regex pattern is a special language used to represent generic text, numbers or symbols so it can be used to extract texts that conform to that pattern
#Here the '\s' matches any whitespace character. By adding a '+' notation at the end will make the pattern match at least 1 or more spaces. So, this pattern will match even tab '\t' characters as well.
import re
regex = re.compile('\s+')
text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""
re.split('\s+',text)
#pattern = '\s+'
regex_digit = '\d+' #At least one digit or more 
re.findall(regex_digit,text)
get_ipython().run_line_magic('load', 'regexpression.py')
# %load regexpression.py
import re
#Regular Expression

regex = r"([a-zA-Z]+) (\d+)"
print (regex)
pattern = r"Sajin"
sequenc = "Sajin"
if re.match(pattern, sequenc):
    print (" Exact match")
else:
    print ( "No match -sorry")
    
re.search(Sa..n,pattern).group()
# %load regexpression.py
import re
#Regular Expression
regex = r"([a-zA-Z]+) (\d+)"
print (regex)
pattern = r"Sajin"
sequenc = "Sajin"
if re.match(pattern, sequenc):
    print (" Exact match")
else:
    print ( "No match -sorry")
    
