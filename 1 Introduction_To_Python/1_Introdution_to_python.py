#Writen_By Hemanth digitalhemanth
#Python Language Introduction
'''
# Python is a widely used general-purpose, high level programming language.
# It was initially designed by Guido van Rossum in 1991 and developed by Python Software Foundation.
# It was mainly developed for emphasis on code readability, and its syntax allows programmers to express
   concepts in fewer lines of code.'''

#Python is a programming language that lets you work quickly and integrate systems more efficiently.
'''
There are two major Python versions- Python 2 and Python 3. Both are quite different.

'''
 #Division operator 
 #print function 
 #Unicode 
 #xrange
 #Error Handling 
 #_future_ module 

'''
           #Division operator : 
                python 3.x code in python 2.x, it can be dangerous if integer division changes
           go unnoticed (since it doesn’t raise any error).
           #print function : 
                       This is the most well known change. In this the print function in 
                       Python 2.x is replaced by print() function in Python 3.x,i.e, to print in 
                       Python 3.x an extra pair of parenthesis is required.
            
           #Unicode         :
                         In Python 2, implicit str type is ASCII. But in Python 3.x implicit str type is Unicode
           #xrange        : 

                           In Python 3.x, the range function now does what xrange does in Python 2.x,
                            so to keep our code portable, we might want to stick to using range instead.
                            So Python 3.x’s range function is xrange from Python 2.x.
           #Error Handling : 
                          There is a small change in error handling in both versions. In python 3.x,
                          ‘as’ keyword is required. 

                           try: 
                               trying_to_check_error 
                               except NameError, err: 
                               print err, 'Error Caused'   # Would not work in Python 3.x 
               

           #_future_ module : 
                           This is basically not a difference between two version, 
                           but useful thing to mention here. The idea of __future__ module is to help 
                           in migration. We can use Python 3.x If we are planning Python 3.x support in
                           our 2.x code,we can ise_future_ imports it in our code.

'''

