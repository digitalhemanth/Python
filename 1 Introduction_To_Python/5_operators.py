#operators in python

'''Operators are special symbols in Python that carry out arithmetic or logical computation.
 The value that the operator operates on is called the operand.'''

'''
For example:
>>> 2+3
5
'''
#Arithmetic operators

'''Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.'''
# +	 Add two operands or unary plus	x + y
# -	Subtract right operand from the left or unary minus	x - y
# *	Multiply two operands	x * y
# /	Divide left operand by the right one (always results into float)	x / y
# %	Modulus - remainder of the division of left operand by the right	x % y (remainder of x/y)
# //	Floor division - division that results into whole number adjusted to the left in the number line	x // y
# **	Exponent - left operand raised to the power of right
#-----------------------------------------------------------------------------------------------------

#Comparison operators

'''Comparison operators are used to compare values. It either returns True or False according to the condition.'''

# >	Greater that - True if left operand is greater than the right	x > y
# <	Less that - True if left operand is less than the right	x < y
# ==	Equal to - True if both operands are equal	x == y
# !=	Not equal to - True if operands are not equal	x != y
# >=	Greater than or equal to - True if left operand is greater than or equal to the right	x >= y
# <=	Less than or equal to - True if left operand is less than or equal to the right

#-----------------------------------------------------------------------------------------------------

#Logical operators

'''Logical operators are the and, or, not operators.'''

# and	True if both the operands are true	x and y
# or	True if either of the operands is true	x or y
# not	True if operand is false (complements the operand)	not x

#-----------------------------------------------------------------------------------------------------

#Bitwise operators

'''Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.

For example, 2 is 10 in binary and 7 is 111.

In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)'''

# &	Bitwise AND	x& y = 0 (0000 0000)
# |	Bitwise OR	x | y = 14 (0000 1110)
# ~	Bitwise NOT	~x = -11 (1111 0101)
# ^	Bitwise XOR	x ^ y = 14 (0000 1110)
# >>	Bitwise right shift	x>> 2 = 2 (0000 0010)
# <<	Bitwise left shift	x<< 2 = 40 (0010 1000)

#-----------------------------------------------------------------------------------------------------

# Assignment operators

'''Assignment operators are used in Python to assign values to variables.
a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.
There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.
'''
# =	x = 5	x = 5
# +=	x += 5	x = x + 5
# +=	x += 5	x = x + 5
# -=	x -= 5	x = x - 5
# *=	x *= 5	x = x * 5
# /=	x /= 5	x = x / 5
# %=	x %= 5	x = x % 5
# //=	x //= 5	x = x // 5
# **=	x **= 5	x = x ** 5
# &=	x &= 5	x = x & 5
# |=	x |= 5	x = x | 5
# ^=	x ^= 5	x = x ^ 5
# >>=	x >>= 5	x = x >> 5
# <<=	x <<= 5	x = x << 5

#-----------------------------------------------------------------------------------------------------

#Special operators

'''Python language offers some special type of operators like the identity operator or the membership operator.'''
#-----------------------------------------------------------------------------------------------------

#Identity operators

'''is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. 
Two variables that are equal does not imply that they are identical.'''

# is	True if the operands are identical (refer to the same object)	x is True
# is not	True if the operands are not identical (do not refer to the same object)

#-----------------------------------------------------------------------------------------------------

# Membership operators

'''in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
In a dictionary we can only test for presence of key, not the value.'''

# in	True if value/variable is found in the sequence	
# not in	True if value/variable is not found in the sequence

