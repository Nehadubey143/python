# Exponentiation ("**")

# Used to calculate power of a number 
# 4 pe power 2 => 16

# Example:-
#  a = 5 
#  b = 3 
#  print("output: ", a ** b ) Output → 125
# _____________________________

# 2. Assignment Operator

# +=,-=,*=,/=.......................
# _____________________________

# Example:-
# a = 10 
# b = 3

# a = a + b

# a += b

# NOTES :- ( a = a + b ) and ( a += b ) , both are the same thing but , ( a += b ) takes less time to run the code .
# _____________________________

# Time Complexity → time taken by any code to run .
# _____________________________

# Real life example:-

# Ayush has to reach the Rajiv Nagar Metro station . 

# He has 2 options. ( Bus A , and Bus B ) , Kiraya => 25 Rupees 

# Bus A takes 30 mins to reach the Rajiv Nagar Metro station .

# Bus B takes 40 mins to reach the Rajiv Nagar Metro station .
# _____________________________

# 3.Logical Operator :-

# Type of Logical Operators
# and
# or
# not
# _____________________________
# AND Operator
# If both conditions are TRUE → TRUE
# Otherwise → FALSE
# _____________________________
# OR Operator
# If both conditions are FALSE → FALSE
# Otherwise → TRUE
# _____________________________
# NOT Operator
# It gives the opposite value.
# _____________________________
# Example 1:-
# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a)
# _____________________________

# Example 2:-
# a = True 
# b = False 

# print( a and b )
# _____________________________

# Example 3:-
# a = True 
# b = False 
# c = True 


# print( a or b )  ## True or False → True 

# print( a or c)  ## True or True → true 
# _____________________________

# Example 4:-
# a = True 
# b = False 

# print(not a)  ## False 
# print(not b ) ## True
# _____________________________

# 4. Bitwise Operator
# Binary Number
# 0000 => 0
# 0001 => 1
# 0010 => 2
# 0011 => 3
# 0100 => 4
# 0101 => 5
# 0110 => 6
# 0111 => 7
# 1000 => 8
# 1001 => 9
# 1010 => 10  => A
# 1011 => 11  => B
# 1100 => 12  => C
# 1101 => 13  => D
# 1110 => 14  => E
# 1111 => 15  => F

# TRUE → 1
# False → 0
# _____________________________

# Rules:-
# Bitwise &
# If both cases are 1, it gives 1 otherwise it gives 0.
# Bitwise |
# If both cases are 0, it gives 0 otherwise it gives 1.
# _____________________________

# Example Calculation:-

#    3  5  6
# + 2  4  3
# -----------
#   5  9  9
# _____________________________

# Example 1:-

# a = 10 , binary number of 10 → 1010
# b = 3   , binary number of 3 → 0011

# print(a & b)

# Binary Calculation:
#     1  0  1  0   => binary of 10
# &  0  0  1  1   => binary of 3
# ---------------
#    0  0  1  0   => binary of 2
# _____________________________

# Example 2:-

# a = 14 , binary number of 14 → 1110 
# b = 11 , binary number of 11 → 1011

# print(a & b)

#  1  1  1  0
# & 1  0  1  1
# ---------------
#   1  0  1  0  =>  binary number of 10
# _____________________________

# Example 3:-

# a = 14 ,binary number of 14 → 1110  
# b = 11 ,binary number of 11 → 1011

# print(a | b)

#    1  1  1  0
# |  1  0  1  1
# ----------------
#    1  1  1  1  => binary number of 15
