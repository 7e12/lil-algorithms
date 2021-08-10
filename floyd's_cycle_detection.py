# author:  7e12
# file:    floyd's_cycle_detection.py
# date:    11 Aug 2021
# version: v1.0.0
# brief:   The Floyd's "tortoise and hare" cycle detection algorithm implementation

import random as rd

# User-defined macros
SEQUENCE_SIZE = 100

# The Floyd's "tortoise and hare" cycle detection algorithm implementation
def floyd(sequence):
    tortoise = sequence[0]
    hare = sequence[sequence[0]]

    # The hare moves twice as quickly as the tortoise
    # The distance between them increases by one at each step
    # Eventually they will both be inside the cycle
    while tortoise != hare:
        tortoise = sequence[tortoise]
        hare = sequence[sequence[hare]]

    # The hare moves inside the circle one step at a time
    # The tortoise (reset to 0) moves towards the circle
    # They will intersect at the beginning of the circle
    tortoise = 0
    while tortoise != hare:
        index = tortoise
        tortoise = sequence[tortoise]
        hare = sequence[hare]

    return tortoise, index

# Main program
def main():
    print("FLOYD'S \"TORTOISE AND HARE\" CYCLE DETECTION ALGORITHM")

    # Create the sequence for testing
    sequence = rd.sample(range(1, SEQUENCE_SIZE + 1), SEQUENCE_SIZE)

    # Create the duplicate number and insert to the sequence for testing
    number = rd.randint(1, SEQUENCE_SIZE)
    sequence.insert(rd.randint(0, SEQUENCE_SIZE), number)

    # Print the test sample
    print("Sequence:")
    print(sequence)
    print("Test number:", number)

    # Print the result
    duplicate_number, duplicate_index = floyd(sequence)
    print("Result:")
    print("Duplicate number:", duplicate_number)
    print("First duplicate index:", duplicate_index)

if __name__ == "__main__":
    main()
