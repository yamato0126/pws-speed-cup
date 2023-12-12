import random
import csv

def rand(x):
    """Return a random integer in the range [0, x)."""
    return random.randint(0, x - 1)

def create_p_matrix(n, m, c):
    """Create a matrix of size n x m with each element as min{Rand(c), Rand(c)}."""
    return [[min(rand(c), rand(c)) for _ in range(m)] for _ in range(n)]

def create_r_matrix(n, m, c):
    """Create a matrix of size n x m with each element as Rand(c)."""
    return [[rand(c) for _ in range(m)] for _ in range(n)]

def concatenate_matrices(matrix1, matrix2):
    """Concatenate two matrices horizontally."""
    return [row1 + row2 for row1, row2 in zip(matrix1, matrix2)]

def save_to_csv(matrix, filename):
    """Save the matrix to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(matrix)

# Parameters
n = 10**5
m_p = 8
m_r = 10
c = 10
filename = '../Docker/src/o.csv'

# Create the matrix and save it to a CSV file
p_matrix = create_p_matrix(n, m_p, c)
r_matrix = create_r_matrix(n, m_r, c)
concatenated_matrix = concatenate_matrices(p_matrix, r_matrix)
save_to_csv(concatenated_matrix, filename)
