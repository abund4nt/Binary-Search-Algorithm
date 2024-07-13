def binary_search(arr, low, high, x):

    if high >= low:
        
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
        
    else:
        return -1
    
arr = [ 2, 3, 4, 10, 40, 80, 120, 240, 340, 660, 1100, 1700, 2900]
x = 1100

result = binary_search(arr, 0, len(arr), x)

if result != -1:
    print(f"Element present at index {str(result)} (0+)")
else:
    print("Element is not present in array")