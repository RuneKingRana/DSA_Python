def matrix(rows, cols, name):
    print(f"Enter elements of the {name} matrix:", end = " ")
    return [[int(input()) for j in range(cols)] for i in range(rows)]

def multiply(arr1, arr2, x, y, z):
    # Initialize result matrix with zeros
    arr3 = [[0 for num in range(z)] for num in range(x)]
    for i in range(x):
        for j in range(z):
            for k in range(y):
                arr3[i][j] += arr1[i][k] * arr2[k][j]
    return arr3

def main():
    m = int(input("Enter rows of 1st matrix: "))
    n = int(input("Enter columns of the 1st matrix: "))
    o = int(input("Enter rows of 2nd matrix: "))
    if n != o:
        print("First matrix column number and second matrix row number should be same.")
        return
    p = int(input("Enter columns of the 2nd matrix: "))
    q = int(input("Enter rows of 3rd matrix: "))
    if p != q:
        print("Second matrix column number and Third matrix row number should be same.")
        return
    r = int(input("Enter columns of the 3rd matrix: "))

    a = matrix(m, n, "1st")
    b = matrix(o, p, "2nd")
    c = matrix(q, r, "3rd")
    r1 = multiply(a, b, m, n, p)
    r2 = multiply(r1, c, m, p, r)

    print("Resultant matrix:")
    for row in r2:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
