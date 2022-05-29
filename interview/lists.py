
from cgitb import reset


temp = [9,6,3,1,6,8,9,2,1]
val = iter(temp)
print(next(val))

result = []
[result.append(x) for x in temp if x not in result ]
print(len(result))

x = list(set(temp))
print(x)
"""
lists = []
print(lists)
statement = 'Hey I am Hemanth'
lists= statement.split()
print(lists)
print(lists[2])
print(lists[::-1])
"""





