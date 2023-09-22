m1, n1 = map(int, input("Enter the number of rows and cols of matrix 1: ").split())
m2, n2 = map(int, input("Enter the number of rows and cols of matrix 2: ").split())
matrix1 = []
matrix2 = []
for i in range(m1):
    row = list(map(int, input().split()))
    matrix1.append(row)
for i in range(m2):
    row = list(map(int, input().split()))
    matrix2.append(row)
    
row1 = len(matrix1)
col1 = len(matrix1[0])
row2 = len(matrix2)
col2 = len(matrix2[0])

if col1 != row2:
    print("Cannot be multiplied!")

else:
    result = [[0 for _ in range(col2)] for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] = matrix1[i][k] * matrix2[k][j]

for i in result:
    print(i)

    
