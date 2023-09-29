if __name__ == '__main__':
    # n = int(input())
    n=3

    # valid number of scores allowed
    min = 2
    max = 10
    if(min <= n <= max):
        print("valid %d" % n)

        # arr = map(int, input().split())
        arr = map(int, ['11','22','33'])
        # copy map object to a list that can be iterable
        myList = list(arr)
        print(len(myList))

        print("cast map object to list: first in list: %d" % myList[0])

        # myList.sort()
        # print(myList)
        myList.reverse()
        print(myList)

        # m = max(myList())
        # print("max from list: ", m)
        
    else:
        print("invalid %d" % n)