def maxmin(a):
    min = a[0]
    max = a[0]
    for i in a:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min,max

n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for i in range(n)]
mini,maxi = maxmin(arr)
print("Minimum element is:", mini)
print("Maximum element is:", maxi)
