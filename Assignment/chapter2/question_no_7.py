
def matrix_multiplication(M, N):

    R = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
        
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                R[i][j] += M[i][k] * N[k][j]

    for i in range(0, 3):
        for j in range(0, 3):

            print(R[i][j], end =" ")
        print("\n", end ="")

# First matrix. M is a list
M = [[4, 1, -8],
	[7, 4, 4],
	[4, -8, 1]]

# Second matrix. N is a list
N = [[4, 1,-8],
	[7,4,4],
	[4, -8, 1]]
# Call matrix_multiplication function
matrix_multiplication(M, N)


