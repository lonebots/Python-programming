def rotatematrix(n, mat):

    row = 0
    col = 0
    m = n
    num = n
    '''
       row - Staring row index
       m - ending row index
       col - starting column index
       n - ending column index
       i - iterator
    '''
    while (row < m and col < n):

        if (row + 1 == m or col + 1 == n):
            break
        ''' Store the first element of next row, this
         element will replace first element of current row '''

        prev = mat[row + 1][col]

        # Move elements of first row from the remaining rows
        for i in range(col, n):

            curr = mat[row][i]
            mat[row][i] = prev
            prev = curr

        row = row + 1

        # Move elements of last column from the remaining columns
        for i in range(row, m):

            curr = mat[i][n - 1]
            mat[i][n - 1] = prev
            prev = curr

        n = n - 1

        #Move elements of last row from the remaining rows
        if (row < m):

            for i in range(n - 1, col - 1, -1):

                curr = mat[m - 1][i]
                mat[m - 1][i] = prev
                prev = curr

        m = m - 1

        # Move elements of first column from the remaining rows
        if (col < n):

            for i in range(m - 1, row - 1, -1):

                curr = mat[i][col]
                mat[i][col] = prev
                prev = curr

        col = col + 1


# Print rotated matrix
    for i in range(num):
        print(*mat[i], sep=" ", end="\n")

n = int(input())
mat = []
for i in range(n):
    temp = list(map(int, input().split()))
    mat.append(temp)

rotatematrix(n, mat)