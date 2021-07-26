import sys
'''
Niko Perry
2/19/21
file: matrixMult

Program: This program reads two matrices from a txt file, 
multiplies them, and prints the result. Matrix 'A' has
dimensions m x n while matrix 'B' has dimensions n x p

Instructions: Compile code with input file as an argument or enter 
after running. 

Input file: The first three lines of the file contain the values m, 
n, and p, each on a line by themselves. Following are two matrices,
A followed by B with no blank lines, of the dimensions specified,
one row per line. Each row entry is separated by a space.
'''
def main():
    A = []
    B = []
    C = read_matrices(A,B)
    C = mult_matrices(A,B,C)
    print('Matrix A contents:')
    print_matrix(A)
    print('\nMatrix B contents:')
    print_matrix(B)
    print('\nMatrix A * B contents:')
    print_matrix(C)

def read_matrices(A,B):
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Enter file name: ')
        file_name = input()
    with open(file_name) as f:
        # store dimensions of the arrays
        m = int(f.readline().rstrip())
        n = int(f.readline().rstrip())
        p = int(f.readline().rstrip()) 
        # Store matrix A
        for row in range(m):
            # Separate each row into an arr
            row = f.readline().strip('\n')
            arr = [int(num) for num in row.split(' ')]
            A.append(arr)
    
        # Store matrix B
        for row in range(n):
            # Separate each row into an arr
            row = f.readline().strip('\n')
            arr = [int(num) for num in row.split(' ')]
            B.append(arr)
    	
        # Allocate matrix C with size m x p
        C = [ [0 for i in range(m)] for j in range(p)]
        return C

def print_matrix(matrix):
    for row in matrix:
        print(row)

def mult_matrices(A,B,C):
    C = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    return C
'''
For some reason this code produces an IndexError: list index out of range

# iterate through rows of A
for i in range(len(A)):
    # iterate through columns of B
    for j in range(len(B[0])):
        # iterate through rows of B
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
'''
# Begin program
if __name__ == '__main__':
    main()
