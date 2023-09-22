row = int(input()) #5 
pascal = []

for i in range(row):#row
    pascal_row = []#appends the row
    for j in range(i+1):#column
        if j == 0 or j == i:
            pascal_row.append(1)
        else:
            temp = pascal[i-1][j-1] + pascal[i-1][j]
            pascal_row.append(temp)
    pascal.append(pascal_row)
print(pascal)
        
