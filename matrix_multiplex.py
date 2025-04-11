def matrix(rows, cols, name):
    print(f"Enter elements of the {name} matrix:", end = " ")
    return [[int(input()) for j in range(cols)] for i in range(rows)]

def multiply(a, b, m, n, p):
    # Initialize result matrix with zeros
    c = [[0 for x in range(p)] for x in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def main():
    m = int(input("Enter rows of 1st matrix: "))
    n = int(input("Enter columns of the 1st matrix: "))
    o = int(input("Enter rows of 2nd matrix: "))
    if n != o:
        print("First matrix column number and second matrix row number should be same.")
        return
    p = int(input("Enter columns of the 2nd matrix: "))

    a = matrix(m, n, "1st")
    b = matrix(o, p, "2nd")
    result = multiply(a, b, m, n, p)

    print("Resultant matrix:")
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
