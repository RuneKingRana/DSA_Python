def quicksort(a):
    stack = [(0, len(a) - 1)]

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        pivot, i = a[high], low - 1
        for j in range(low, high):
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        p = i + 1

        stack.append((low, p - 1))
        stack.append((p + 1, high))


# Driver code
n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for i in range(n)]
quicksort(arr)
#print("The sorted array  in accending order is:",arr)
print("Sorted array is :",end=" ")
for i in range(n):
    print("%d" % arr[i],end=" ")
