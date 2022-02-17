def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if list1[mid] < n:
            low = mid + 1
        elif list1[mid] > n:
            mid = mid - 1
        else:
            return mid
list1 = [10, 20, 30, 40, 50, 60, 70]
n = 40
result = binary_search(list1, n)
if result != -1:
    print("Element are present at index", str(result))
else:
    print("Elements are not present in this list")
