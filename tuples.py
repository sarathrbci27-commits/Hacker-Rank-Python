if __name__ == '__main__':
    n = int(input())  # Read the number of elements in the tuple
    integers = map(int, input().split())  # Read the space-separated integers and convert them to integers
    t = tuple(integers)  # Create a tuple of the integers
    print(hash(t))  # Print the hash value of the tuple
