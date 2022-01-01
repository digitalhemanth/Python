#Lambda:
#Single one line function ,Anoymous function(no name),no def, no return

add = lambda a,b : print(a+b)
add(6,8)

#Map
#The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .

nums = [2,8,6,4]
def sqr(n):
     return n*n
output = list(map(sqr,nums))
print(output)

'''
Syntax: map(fun, iter)
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

'''

nums = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**x, nums))
print(square)
