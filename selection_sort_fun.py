def selection(a):
    for ind in range(len(a)):
        min_index = ind
        for j in range(ind + 1, len(a)):
            # select the minimum element in every iteration
            if a[j] < a[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (a[ind], a[min_index]) = (a[min_index], a[ind])


n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for i in range(n)]
selection(arr)
#print("The sorted array  in accending order is:",arr)
print("Sorted array is :",end=" ")
for i in range(n):
    print("%d" % arr[i],end=" ")