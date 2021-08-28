#What is for loop in Python?

'''
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
'''
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)

#The range() function 
 
''' 
 We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).
We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.
This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.
To force this function to output all the items, we can use the function list().
'''
print(range(10))

#----------------------------------------------------------------------------

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])

#for loop with else
'''
 for loop can have an optional else block as well.
 The else part is executed if the items in the sequence used in for loop exhausts.
 break statement can be used to stop a for loop. In such case, the else part is ignored.
 Hence, a for loop's else part runs if no break occurs.
 '''
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

#-------------------------------------------------------------------------------------------

#What is while loop in Python?

'''
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

We generally use this loop when we don't know beforehand, the number of times to iterate.

Syntax of while Loop in Python

while test_expression:
    Body of while
'''
n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

#-------------------------------------------------------------------------------------------

#while loop with else
'''
Same as that of for loop, we can have an optional else block with while loop as well.
The else part is executed if the condition in the while loop evaluates to False.

The while loop can be terminated with a break statement. In such case, the else part is ignored. Hence, 
a while loop's else part runs if no break occurs and the condition is false.
'''
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


#-------------------------------------------------------------------------------------------
#What is the use of break and continue in Python?

'''
In Python, break and continue statements can alter the flow of a normal loop.

Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.

The break and continue statements are used in these cases.
'''
#Python break statement

'''The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.'''

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

#-------------------------------------------------------------------------------------------
#Python continue statement

'''
The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
'''
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

#-------------------------------------------------------------------------------------------

#What is pass statement in Python?
'''
In Python programming, pass is a null statement.
The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.'''

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

