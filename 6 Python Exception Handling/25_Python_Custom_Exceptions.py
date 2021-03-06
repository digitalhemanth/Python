#Python Custom Exceptions

'''
Python has many built-in exceptions which forces your program to output an error when something in it goes wrong.
         However, sometimes you may need to create custom exceptions that serves your purpose.
     Python, users can define such exceptions by creating a new class. This exception class has to be derived, either directly or indirectly, 
from Exception class. Most of the built-in exceptions are also derived form this class.

'''
    pass
...

>>> raise CustomError
Traceback (most recent call last):
...
__main__.CustomError

>>> raise CustomError("An error occurred")
Traceback (most recent call last):
...
__main__.CustomError: An error occurred

'''
Here, we have created a user-defined exception called CustomError which is derived from the Exception class. This new exception can be raised,
 like other exceptions, using the raise statement with an optional error message.

When we are developing a large Python program, it is a good practice to place all the user-defined 
exceptions that our program raises in a separate file. 
Many standard modules do this. They define their exceptions separately as exceptions.py or errors.py 
(generally but not always).

'''

#Example: User-Defined Exception in Python
'''
n this example, we will illustrate how user-defined exceptions can be used in a program to raise and
catch errors.
             This program will ask the user to enter a number until they guess a stored number correctly.
 To help them figure it out, hint is provided whether their guess is greater than or less than the stored
 number.

User-defined exception class can implement everything a normal class can do, but we generally make
them simple and concise. Most implementations declare a custom base class and derive others exception classes from this base class.
'''
# This concept is made clearer in the following example.
# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")

'''
Here, we have defined a base class called Error.

The other two exceptions (ValueTooSmallError and ValueTooLargeError) that are actually raised
 by our program are derived from this class. This is the standard way to define user-defined 
 exceptions in Python programming, but you are not limited to this way only.
'''
