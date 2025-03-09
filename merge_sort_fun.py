def mergesort(a):
    n = len(a)
    curr = 1

    while curr < n:
        for left in range(0, n, 2 * curr):
            mid = min(left + curr - 1, n - 1)
            right = min(left + 2 * curr - 1, n - 1)

            L, R = a[left:mid + 1], a[mid + 1:right + 1]
            i = j = 0
            k = left

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                a[k] = R[j]
                j += 1
                k += 1

        curr *= 2

# Driver code
n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for _ in range(n)]
mergesort(arr)
#print("The sorted array  in accending order is:",arr)
print("Sorted array is :",end=" ")
for i in range(n):
    print("%d" % arr[i],end=" ")
