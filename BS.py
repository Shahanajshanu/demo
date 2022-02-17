def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if list1[mid] < n:
            low = mid + 1
        elif list1[mid] > n:
            high = mid - 1
        else:
            return mid
list1 = [10, 36, 34, 50, 44, 54, 20]
n = int(input("Enter: "))
result = binary_search(list1, n)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Elements are not present in this list1")
