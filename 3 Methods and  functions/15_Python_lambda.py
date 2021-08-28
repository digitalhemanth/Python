#Python lambda

'''
In Python, anonymous function means that a function is without a name.
As we already know that def keyword is used to define the normal functions and the lambda keyword
is used to create anonymous functions.
'''
#It has the following syntax:
#     lambda arguments: expression 

''' 
- This function can have any number of arguments but only one expression,
which is evaluated and returned.
- One is free to use lambda functions wherever function objects are required.
- You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
- It has various uses in particular fields of programming besides other types of expressions in functions.
'''
# Python code to illustrate cube of a number  
# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y; 
g = lambda x: x*x*x 
print(g(7)) 
print(cube(5))


#Use of lambda() with filter()

'''
The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence “sequence”, 
for which the function returns True.
'''
#Here is a small program that returns the odd numbers from an input list:

# Python code to illustrate 
# filter() with lambda() 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)

#Use of lambda() with map()

'''
The map() function in Python takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new list is returned which 
contains all the lambda modified items returned by that function for each item. 
'''
# Python code to illustrate  
# map() with lambda()  
# to get double of a list. 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 