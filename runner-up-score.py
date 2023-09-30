if __name__ == '__main__':
    n = int(input())
    
    # valid number of scores allowed
    min = 2
    max = 10
    if(min <= n <= max):
       
        arr = map(int, input().split())
       
        # copy map object to a list that can be iterable
        myList = list(arr)
       
        # reverse sort the list
        myList.sort()
        myList.reverse()
       
        # walk this list from highest score to next lower score - that will be the runner
        # up score and address the possibilities of multiple highest scores

        start = 0
        nxt = 1

        # walk the reverse sorted list from highest to next highest
        while(myList[start] <= myList[nxt]):
            start += 1
            nxt += 1

        # done 
        print(myList[nxt])
        
    else:
        print("invalid number of scores in list: %d" % n)