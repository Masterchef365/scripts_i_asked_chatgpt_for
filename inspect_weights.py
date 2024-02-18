#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from sys import argv

def visualize_matrix(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title('Matrix Visualization')
    plt.show()


def is_positive_semidefinite(matrix):
    # Check if the matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        return False

    # Compute eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)
    print(eigenvalues)

    # Check if all eigenvalues are non-negative
    return np.all(eigenvalues >= 0)


if __name__ == "__main__":
    try:
        file_path = argv[1]
    except:
        print(f"Usage: {argv[0]} <weights.csv>")
        exit()

    
    try:
        # Load matrix directly using numpy.loadtxt
        matrix = np.loadtxt(file_path, delimiter=',')

        print("Is is positive semi-definite: ", is_positive_semidefinite(matrix))
        
        # Check if the matrix is square
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("The matrix is not square.")
        
        visualize_matrix(matrix)
    except Exception as e:
        print(f"Error: {e}")
