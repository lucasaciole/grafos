import copy

def power_method(M, w0, k):
    result = copy.deepcopy(M)
    result = multiply_matrix([w0], result)
    for _ in range(k): result = multiply_matrix(result, M)
    return result



def multiply_matrix(A, B):
    result = [[0]*len(B[0]) for i in range(len(A))]
    # iterate through rows of A
    for i in range(len(A)):
       # iterate through columns of B
       for j in range(len(B[0])):
           # iterate through rows of B
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    return result

if __name__ == "__main__":
    matrix_file = open("snakes_matrix.txt", "r")
    matrix = [list(map(float,line.split(","))) for line in matrix_file]
    w = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = power_method(matrix,w,100)
    print(result[35])
