def print_spiral(n, mat):
    k = 0
    l = 0
    m = n
    c = 1
    last = m * n
    while (k < n and l < n):

        #printing the first column
        for i in range(k, m):
            if (c == last):
                print(mat[i][l], end="")

            else:
                print(mat[i][l], end=" ")
            c += 1
        l += 1

        #printing the last row
        for i in range(l, n):
            if (c == last):
                print(mat[m - 1][i], end="")

            else:
                print(mat[m - 1][i], end=" ")
            c += 1
        m -= 1

        if (l < n):
            #printing the last column reverse
            for i in range(m - 1, k - 1, -1):
                if (c == last):
                    print(mat[i][n - 1], end="")

                else:
                    print(mat[i][n - 1], end=" ")
                c += 1
            n -= 1

        if (k < m):
            #printing the topmost row reverse
            for i in range(n - 1, l - 1, -1):
                if (c == last):
                    print(mat[k][i], end="")
                else:
                    print(mat[k][i], end=" ")
                c += 1
            k += 1


n = int(input())
mat = []
for i in range(n):
    temp = list(map(int, input().split()))
    mat.append(temp)

#print(mat)
print_spiral(n, mat)
