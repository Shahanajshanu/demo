arr = [5, 8, 2, 0, 4]
temp = 0
print("Elements in orginal array: ")
for i in range(0, len(arr)):
    print(arr[i], end="")

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print()

print("Elements of an array in assending  order: ")
for i in range(0, len(arr)):
    print(arr[i], end="")
