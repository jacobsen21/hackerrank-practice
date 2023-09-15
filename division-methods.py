if __name__ == '__main__':
    a = int(input())
    b = int(input())

    # check constraints
    # to avoid division by zero error, b cannot = 0

    # perform division operations
    if(b != 0):
        print( a // b )
        print( a / b )