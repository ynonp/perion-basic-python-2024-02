import numpy as np

# Build a 1d array with 100 elements with values [2, 4, 6, 8, ... 200] (Hint: arange)

if __name__ == "__main__":
    print(np.arange(1, 101) * 2)
    print(np.arange(2, 201, 2))

# Build a 2d (10, 10) array representing the multiplication table: (Hint: broadcasting)
if __name__ == "__main__":
    np.arange(1, 11).reshape(10, 1) * np.arange(1, 11)

# From the above array (multiplication table), extract only the numbers in the diagonal: 1, 4, 9, ... , 100.
if __name__ == "__main__":
    a = np.arange(1, 11).reshape(10, 1) * np.arange(1, 11)
    np.diag(a)

# Read on the module np.random, then create a random 1d-array of 10 integer elements, then print only the odd values. (Hint: Boolean mask)
if __name__ == "__main__":
    a = np.random.randint(100, size=(10,))
    a[a % 2 == 1]

# Create a random 2d-array of (10, 10) integer elements, then replace all the odd values with 0 (Hint: np.where).
if __name__ == "__main__":
    a = np.random.randint(100, size=(10, 10))
    a[a % 2 == 1] = 0
    np.where(a % 2 == 1, 0, a)


