my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    total = 0
    for item in list:
        if item % 2 == 1:
            total = total + item
    return total
print(sum_odds(my_list))