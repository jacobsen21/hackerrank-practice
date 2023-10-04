if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # example 
    # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    # newlist = [x for x in fruits if "a" in x]
    # print(newlist)

    # generate initial list of permutations from x,y,z
    iters = [[i, j, k] for i in range(x+1) \
             for j in range(y+1) \
             for k in range(z+1)]
    print(iters)

    # create comprehensive new list that only includes permutations != 3
    newiters =  [[i, j, k] for i in range(x+1) \
        for j in range(y+1) \
        for k in range(z+1) \
        if i+j+k != n]
    print(newiters)
    