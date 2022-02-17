arr = [10, 30, 40, 20, 15]
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
print("Elements in assending order: ")
for i in range(0, len(arr)):
    print(arr[i], end="")
