# Your code here
def matrix_builder(integer_value):
    matrix = []
    for i in range(integer_value):
        row = []
        for j in range(integer_value):
            row.append(1) #appends 1 to the row j times
        matrix.append(row) #appends the rows to the matrix i times

    return matrix
    
print(matrix_builder(2))