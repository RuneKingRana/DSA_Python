# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = low + (high - low)//2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

'''
n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for i in range(n)]
'''
arr = [ 2, 3, 4, 7, 10, 17, 18, 45, 49, 63]
x = int(input("Enter the element to find: "))

# Function call
result = binary(arr, x)

if result != -1:
    print("Element is present at index:", str(result+1))
else:
    print("Element is not present in array.")
