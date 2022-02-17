print("Enter the order of the 1st Matrix: ")
m, n = list(map(int, input().split()))
print("Enter Row wise values: ")
mat1 = []
for i in range(m):
    print("Enter the row", i, "Values: ")
    row = list(map(int, input().split()))
    mat1.append(row)

print("Enter the order of the 2nd Matrix: ")
p, q = list(map(int, input().split()))
print("Enter Row wise values: ")
mat2 = []
for i in range(p):
    print("Enter the row", i, "Values: ")
    row = list(map(int, input().split()))
    mat2.append(row)

print("Matrix 1", mat1)
print("Matrix 2", mat2)

result = []
for i in range(m):
    row = []
    for j in range(q):
        row.append(0)
    result.append(row)

print("Matrix Multiplication is: ")
for i in range(m):
    for j in range(q):
        for k in range(n):
            result[i][j] += mat1[i][k] * mat2[k][j]

for row in result:
    print(row)


