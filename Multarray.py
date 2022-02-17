print("Enter the order of the 1st matrix: ")
m, n = list(map(int, input().split()))
print("Enter the row wise values: ")
mat1 = []
for i in range(m):
    print("Enter row", i, "value")
    row = list(map(int, input().split()))
    mat1.append(row)

print("Enter the order of the 2nd matrix: ")
p, q = list(map(int, input().split()))
print("Enter row wise values: ")
mat2 = []
for i in range(p):
    print("Enter row", i, "values: ")
    row = list(map(int, input().split()));
    mat2.append(row)

print("Matrix 1: ", mat1)
print("Matrix 2: ", mat2)


result = []
for i in range(m):
    row = []
    for j in range(q):
        row.append(0)
    result.append(row)

print("Matrix Multiplication: ")

# perform matrix multiplication
# using nested for loops
for i in range(m):
    for j in range(q):
        for k in range(n):
            result[i][j] += mat1[i][k] * mat2[k][j]

# matrix printing row wise
for row in result:
    print(row)
