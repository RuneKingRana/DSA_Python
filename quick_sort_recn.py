def partition(a, low, high):
    # choose the rightmost element as pivot
    pivot = a[high]
    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            (a[i], a[j]) = (a[j], a[i])

    (a[i + 1], a[high]) = (a[high], a[i + 1])
    return i + 1

def quicksort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quicksort(a, low, pi - 1)
        quicksort(a, pi + 1, high)


n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for i in range(n)]
quicksort(arr, 0, n - 1)
#print("The sorted array  in accending order is:",arr)
print("Sorted array is :",end=" ")
for i in range(n):
    print("%d" % arr[i],end=" ")
