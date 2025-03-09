def mergesort(a):
    if len(a) > 1:
        #  r is the point where the array is divided into two sub arrays
        r = len(a)//2
        L = a[:r]
        M = a[r:]

        # Sort the two halves
        mergesort(L)
        mergesort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = M[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            a[k] = M[j]
            j += 1
            k += 1

# Driver program
n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for i in range(n)]
mergesort(arr)
#print("The sorted array  in accending order is:",arr)
print("Sorted array is :",end=" ")
for i in range(n):
    print("%d" % arr[i],end=" ")
