from functools import reduce 

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

map_result = list(map(round,list(map(lambda x:x*x, my_floats)),[3]*len(my_floats)))

print(map_result)
