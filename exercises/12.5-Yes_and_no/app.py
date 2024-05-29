the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
new_list = list(map(lambda x: 'wiki' if x == 1 else 'woko', the_bools))
#this maps the lambda function to the_bools
print(new_list)
"""A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

"""