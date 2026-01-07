import sys
import math

# Increase recursion limit for potential deep calls, although not strictly needed here
# sys.setrecursionlimit(10**6) 

def is_prime(num):
    """
    Efficiently checks if a number is prime.
    Handles constraints 0 <= M[i][j] <= 10^4.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check for factors up to sqrt(num)
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_matrix(n, matrix):
    """
    Finds all prime numbers in the matrix and marks their corresponding 
    rows and columns as -1, including the prime cell itself.

    Parameters:
        n (int): Size of the matrix
        matrix (list of list of int): The matrix elements
    Returns:
        list of list of int: Modified matrix based on the problem statement
    """
    
    # 1. Identify all rows and columns containing a prime number.
    # Using sets ensures unique storage and quick look-up.
    prime_rows = set()
    prime_cols = set()
    
    # Iterate through the matrix once to find all prime locations.
    for r in range(n):
        for c in range(n):
            if is_prime(matrix[r][c]):
                prime_rows.add(r)
                prime_cols.add(c)
                
    # 2. Create the modified matrix.
    # It's safer to create a new matrix or copy the old one for modification 
    # to avoid double-marking issues, though here we can modify in place
    # since we only check against the initial prime set.
    
    modified_matrix = [row[:] for row in matrix]

    # Iterate through the matrix again to apply the marking rule.
    for r in range(n):
        for c in range(n):
            # Check if the current cell (r, c) falls into an affected row or column.
            if r in prime_rows or c in prime_cols:
                modified_matrix[r][c] = -1
                
    return modified_matrix

def main():
    """
    Handles input parsing and output printing.
    """
    # Use sys.stdin.read to handle input efficiently in competitive programming environment
    input_data = sys.stdin.read().strip().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])  # First input is the size of the matrix
    matrix = []
    
    # Populate the matrix from the rest of the input data
    index = 1
    try:
        for i in range(n):
            row = []
            for j in range(n):
                row.append(int(input_data[index]))
                index += 1
            matrix.append(row)
    except IndexError:
        # Handle cases where input might be incomplete
        return

    # Call user logic function
    modified_matrix = prime_matrix(n, matrix)
    
    # Print the modified matrix in the required format
    # " ".join(map(str, row)) ensures single spaces between elements
    for row in modified_matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()