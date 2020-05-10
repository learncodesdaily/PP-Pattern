# Function to print the desired
# Alphabet Z Pattern
def alphabetPattern(N):
    # Declaring the values of Right,
    # Left and Diagonal values
    Top, Bottom, Diagonal = 1, 1, N - 1

    # Loop for printing the first row
    for index in range(N):
        print(Top, end=' ')
        Top += 1
    print()

    # Main Loop for the rows from (2 to n-1)
    for index in range(1, N - 1):

        # Spaces for the diagonals
        for side_index in range(2 * (N - index - 1)):
            print(' ', end='')

            # Printing the diagonal values
        print(Diagonal, end='')
        Diagonal -= 1
        print()

        # Loop for printing the last row
    for index in range(N):
        print(Bottom, end=' ')
        Bottom += 1


# Driver Code

# Number of rows
N = 5
alphabetPattern(N)