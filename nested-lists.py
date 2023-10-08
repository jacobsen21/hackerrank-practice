if __name__ == '__main__':

    # records = []

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    #     records.append([name, score])

    # debug 
    n = 4
    records = [['first', 3.33], ['breaker19', 3.33], ['third', 3.33], ['second', 232.22]]
   
    # print(records)
    # min/max
    # print("max: ", max(records))
    # print("min: ", min(records))
   
    # initial alpha sort to get names in alpha order
    records.sort()

    print("initial alpha sort on names")
    print(records)

    # sort by scores
    records.sort(key=lambda x : x[1]) # x[element 0 or 1]
    
    print("sorted low to hi scores: ") 
    print(records)

    print("lowest score: ")
    print(records[0])

    print("2nd lowest score: ")
    print(records[1])

    # set base name and score values from second lowest score
    secname, secscore = records[1]

    # print("sec name: ")
    print(secname)
    
    # set counters for duplicate search
    m = 2

    # compare for duplicate second lowest scores
    while m < n:

        # set individual name and score elements from current record
        name, score = records[m]     

        # if score is equal to seclow base then print name 
        if(score == secscore):
            print(name)
            #break
            # keep looking, just don't print matching dupe names
        m = m + 1

    