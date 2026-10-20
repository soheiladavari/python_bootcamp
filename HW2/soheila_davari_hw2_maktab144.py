#2
matrix = [ 
[1, 2, 3],
[4, 5, 6], 
[7, 8, 9]
]
# transposed=[]
# for col in range(len(matrix[0])):
#     new_row=[]
#     for row in range(len(matrix)):
#         new_row.append(matrix[row][col])
#     transposed.append(new_row)

# print(transposed)
transposed=[
    [row[i] for row in matrix]
    for i in range(len(matrix[0]))
]
print(transposed)

print(matrix[1:])
