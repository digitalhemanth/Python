#What are exceptions in Python?

'''
Python has many built-in exceptions which forces your program to output an error when something in it goes wrong.
              When these exceptions occur, it causes the current process to stop and passes it to 
the calling process until it is handled. If not handled, our program will crash.

              For example, if function A calls function B which in turn calls function C and an exception 
occurs in function C. If it is not handled in C, the exception passes to B and then to A.

If never handled, an error message is spit out and our program come to a sudden, unexpected halt.
'''
#Catching Exceptions in Python

''' 
In Python, exceptions can be handled using a try statement.

A critical operation which can raise exception is placed inside the try clause and the code that handles exception
is written in except clause.

'''
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)


#Catching Specific Exceptions in Python 

'''
A try clause can have any number of except clause to handle them differently but only one will be executed
in case an exception occurs.
'''
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

#Raising Exceptions
'''
In Python programming, exceptions are raised when corresponding errors occur at run time, but we can forcefully 
raise it using the keyword raise.
'''

#try...finally

'''
The try statement in Python can have an optional finally clause. This clause is executed no matter what, 
and is generally used to release external resources.
'''

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

