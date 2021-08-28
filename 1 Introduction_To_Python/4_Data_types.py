#Data Types in Python
          
'''           * Python Numbers
              * Python List
              * Python Tuple
              * Python Strings
              * Python Set
              * Python Dictionary
'''


#Conversion between data types

# @1 Python Numbers

''' Integers, floating point numbers and complex numbers falls under Python numbers category.
    They are defined as int, float and complex class in Python.

    We can use the type() function to know which class a variable or a value belongs to and the 
    isinstance() function to check if an object belongs to a particular class.
'''
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


# @2 Python List

'''List is an ordered sequence of items. It is one of the most used datatype in Python and is
   very flexible. All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed
 within brackets [ ].'''

A = [1, 2.2, 'python']
print(A)


''' dis advantage : not sartable , using keywords only we can retrive data in the list ''' 

# @3 Python Tuple

'''Tuple is an ordered sequence of items same as list.
   The only difference is that tuples are immutable. Tuples once created cannot be modified.

   Tuples are used to write-protect data and are usually faster than list as it cannot change
   dynamically.

   It is defined within parentheses () where items are separated by commas.
'''
t = (5,'program', 1+3j)
print(t)

# @4 Python Strings

''' String is sequence of Unicode characters.
      We can use single quotes or double quotes to represent strings. 
      Multi-line strings can be denoted using triple quotes,
'''
      #''' or """.
s = "This is a string"
ss = "hemanth is  HACKER"
print(ss)

sss = '"Hemanth" is a Hackerand Programmer'
print(sss)

h = ''' hi hemanth 
        welcome to python
        say hai '''
print(h)
# sring methods 
name = 'hemanth'
print(name.upper())

name = 'HELO WORLD '
print(name.lower())

name = 'hemanth kumar'
print(len(name))

name = 'hemanth kumar'
print(name.split())


# @5 Python Set
'''Set is an unordered collection of unique items.
Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.
'''
a = {5,2,3,1,4}

setsval = {3,6,8,1,0,5}
print(setsval)

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

#Python Dictionary

'''Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data.
Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

In Python, dictionaries are defined within braces {} with each item being a pair in the
form key:value. Key and value can be of any type.
''' 
d = {1:'value','key':2}
type(d)

#Conversion between data types
'''We can convert between different data types by using different type conversion functions 
   like int(), float(), str() etc.'''

float(5)
int(10.6)
int(-10.6)
str(25)

