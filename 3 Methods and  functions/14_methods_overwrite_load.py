#Python | Method Overloading

'''
Like other languages (for example method overloading in C++) do, python does not supports method overloading.
We may overload the methods but can only use the latest defined method.
'''

# First product method. 
# Takes two argument and print their 
# product 
def product(a, b): 
    p = a * b 
    print(p) 
      
# Second product method 
# Takes three argument and print their 
# product 
def product_d(a, b, c): 
    p = a * b*c 
    print(p) 
  
# Uncommenting the below line shows an error     
# product(4, 5) 


#Operator Overloading in Python

'''
Operator Overloading means giving extended meaning beyond their predefined operational meaning.
For example operator + is used to add two integers as well as join two strings and merge two lists. 
It is achievable because ‘+’ operator is overloaded by int class and str class.
 You might  have noticed that the same built-in operator or function shows different behavior for
  objects of different classes, this is called Operator Overloading.

'''

# Python program to show use of 
# + operator for different purposes. 
  
print(1 + 2) 
  
# concatenate two strings 
print("Hi"+"Helo")  
  
# Product two numbers 
print(3 * 4) 
  
# Repeat the String 
print("Helo"*4) 

#How to overload the operators in Python?
'''
Consider that we have two objects which are a physical representation of a class (user-defined data type)
and we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know how to add two objects. So we define a method for an operator and that process is called operator overloading. We can overload all existing operators but we can’t create a new operator. To perform operator overloading, Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator.
For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.

'''
#Overloading binary + operator in Python :
'''When we use an operator on user defined data types then automatically a special function or magic function 
associated with that operator is invoked. Changing the behavior of operator is as simple as changing the behavior 
of method or function. You define methods in your class and operators work according to that behavior defined in methods. When we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined. 
There by changing this magic method’s code, we can give extra meaning to the + operator.
'''

# Python Program illustrate how  
# to overload an binary + operator 
  
class A: 
    def __init__(self, a): 
        self.a = a 
  
    # adding two objects  
    def __add__(self, o): 
        return self.a + o.a  
ob1 = A(1) 
ob2 = A(2) 
ob3 = A("Geeks") 
ob4 = A("For") 
  
print(ob1 + ob2) 
print(ob3 + ob4) 

#OUTPUT 
#3
#GeeksFor 

#Overloading comparison operators in Python :

# Python program to overload 
# a comparison operators  
  
class B: 
    def __init__(self, a): 
        self.a = a 
    def __gt__(self, other): 
        if(self.a>other.a): 
            return True
        else: 
            return False
ob1 = B(2) 
ob2 = B(3) 
if(ob1>ob2): 
    print("ob1 is greater than ob2") 
else: 
    print("ob2 is greater than ob1") 

