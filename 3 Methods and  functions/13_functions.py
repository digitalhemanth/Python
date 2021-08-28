#Functions in Python

''' 
A function is a set of statements that take inputs, do some specific computation and produces output.
The idea is to put some commonly or repeatedly done task together and make a function,
so that instead of writing the same code again and again for different inputs, we can call the function.
Python provides built-in functions like print(), etc. but we can also create your own functions.
 These functions are called user-defined functions.
 '''

 # A simple Python function to check 
# whether x is even or odd 
def evenOdd( x ): 
    if (x % 2 == 0): 
        print ("even")
    else: 
        print ("odd")
  
# Driver code 
evenOdd(2) 
evenOdd(3) 

#Pass by Reference or pass by value?
'''
One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created.
Parameter passing in Python is same as reference passing in Java.
'''

# Here x is a new reference to same list lst 
def myFun(x): 
   x[0] = 20
  
# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst)  


#Default arguments:

'''
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
The following example illustrates Default arguments.
'''
# Python program to demonstrate 
# default arguments 
def my_Fun(x, y=50): 
    print("x: ", x) 
    print("y: ", y) 
  
# Driver code (We call myFun() with only 
# argument) 
my_Fun(10) 

#Keyword arguments:
'''
The idea is to allow caller to specify argument name with values so that caller does not need 
to remember order of parameters.
'''
# Python program to demonstrate Keyword Arguments 
def student(firstname, lastname):  
     print(firstname, lastname)  
    
    
# Keyword arguments                   
student(firstname ='Hemanth', lastname ='Kumar')     


#Variable length arguments:
'''We can have both normal and keyword variable number of arguments. '''
# Python program to illustrate   
# *args for variable number of arguments 
def myyFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myyFun('Hello', 'Welcome', 'to', 'world')


# Python program to illustrate   
# *kargs for variable number of keyword arguments 
  
def myFunn(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFunn(first ='Hello', mid ='for', last='Hem') 

#Anonymous functions: 
'''In Python, anonymous function means that a function is without a name. 
As we already know that def keyword is used to define the normal functions and the 
lambda keyword is used to create anonymous functions.
'''


