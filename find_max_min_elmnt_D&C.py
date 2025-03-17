def maxmin(a, low, high):
    if low == high:
        return a[low], a[low]  # Single element case

    if high == low + 1:
        if a[low] < a[high]:
            return a[low], a[high]
        else:
            return a[high], a[low]

    mid = (low + high) // 2
    min1, max1 = maxmin(a, low, mid)
    min2, max2 = maxmin(a, mid + 1, high)

    return min(min1, min2), max(max1, max2)


# Driver code
n = int(input("Enter the number of elements: "))
print("Enter elements: ")
arr = [int(input()) for i in range(n)]

mini, maxi = maxmin(arr, 0, n - 1)
print("Minimum element: ", mini)
print("Maximum element: ",maxi)
