# coding: utf-8
# %load q2-lowest_mark.py
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakinami', 19], ['Vikas', 21]]
dict_stud = dict(students)
dict_stud
dict_stud.values()
list1 = dict_stud.values()
list2 = sorted(set(list1))
list2
low1 = list2[0]
low2 = list2[1]
keys_have_value = [k for k,v in dict_stud.items() if v== low1]
keys_have_value 
keys_have_value1 = [k for k,v in dict_stud.items() if v== low2]
keys_have_value1
keys_have_value1.sort()
for name in keys_have_value1:
    print(name)
    
