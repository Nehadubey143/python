# Python List

# my_list = ["Rohit", "ROhan", "Vivek", "ANkit", 55 , True, False, 44.5]

# print(my_list) → Output = ["Rohit", "ROhan", "Vivek", "ANkit", 55 , True, False, 44.5]

# List Features
#  A list can contain multiple types of value .
# It is enclosed with Square bracket “[ ]”
# It is mutable 
# ____________________________

# List Indexing 

# There are 2 types of indexing methods 
# That are used to access or print any element of any list 
# ____________________________

# 1. Positive Indexing OR +Ve Indexing :-

# It always starts with 0

# Example:-

#               0       1          2            3        4 → Indexing 
# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# print(my_list[2])  → Output = Gulam

# print(my_list[4]) → Output = 55.6
# ____________________________ 

# 2. Negative Indexing OR -Ve Indexing :-

# It always starts with -1

# Example:-

#                  -5    -4      -3            -2      -1 → Indexing 
# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# print(my_list[ -4 ] ) → Output = 22

# print(my_list[ -2 ] ) → Output = -2 
# ____________________________

# List Slicing :-
# There are 2 types of Slicing 
# Two Perameter slicing ( starting point , ending point )

# Three parameter slicing ( Starting point , ending point , gap 



# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# Output

#  [22, "Gulam" , True]

#     0    1        2             3        4  → Indexing 
#  [ 11 , 22, "Gulam" , True , 55.6 ]
# ____________________________
# Slicing Rules :-
# Two Perameter slicing ( starting point , ending point )
# By default the starting point will always be 0.
# By default the ending point will be always EXCLUDED.
# By default the ending point will be the last Index
# ____________________________

# Example 1:-
#              0    1        2         3       4 → Indexing 
# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# print(my_list) 

# print(my_list[ 0 ])  → Output = 11

# print(my_list[ 0 : 3]) 

# Explanation:
# Starting Point = 0 
# Ending point  = 3 ( Excluded) 
# So Final range 0 to 2
# Final Output = [11,  22, "Gulam"]
# ___________________________

# Example 2:-
#              0    1        2         3       4 → Indexing 
# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# print(my_list) 

# print(my_list[ 1 : 4]) 

# Explanation:
# Starting Point = 1
# Ending point  = 4 ( Excluded) 
# So Final range 1 to 3
# Final Output = [22, "Gulam", True ]
# ___________________________

# Example 3:-
#              0    1        2         3       4 → Indexing 
# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# print(my_list) 

# print(my_list[ 0 ])  → Output = 11

# print(my_list[  : 3]) 

# Explanation:
# By default starting Point = 0 
# Ending point  = 3 ( Excluded) 
# So Final range 0 to 2
# Final Output = [11,  22, "Gulam"]
# ___________________________

# Example 4:-
#              0    1        2         3       4 → Indexing 
# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# print(my_list) 

# print(my_list[ 1 : ]) 

# Explanation:
# Starting Point = 1
# By default Ending point  = Last index
# So Final range 1 to Last Index
# Final Output = [22, "Gulam", True, 55.6 ]
# ___________________________

# Example 5:-
#              0    1        2         3       4 → Indexing 
# my_list = [ 11 , 22, "Gulam" , True , 55.6 ]

# print(my_list) 

# print(my_list[  :  ]) 

# Explanation:
# By default Starting Point = 0
# By default Ending point  = Last index
# So Final range 0 to Last Index
# Final Output = [11,  22, "Gulam", True, 55.6 ]
