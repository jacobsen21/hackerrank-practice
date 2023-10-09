if __name__ == '__main__':

    # records = []

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    #     records.append([name, score])

    # n = len(records)

    # debug - hidden test case #2
    n = 5
    records = [['Harsh', 20], ['Beria', 20], ['Varum', 19], 
               ['Kakunami', 19], ['Vikas',21]]
    # expected output: Beria, Harsh
   

    # initial alpha sort to get names in alpha order
    records.sort()

    # sort by scores - x[element 0 or 1]
    records.sort(key=lambda x : x[1])
    
    # set base name and score values from second lowest score
    secname, secscore = records[1]
    print(secname)
    
    # compare for duplicate second lowest scores
    # set counters for duplicate search
    m = 2
    while m < n:

        # set individual name and score elements from current record
        name, score = records[m]     

        # if score is equal to seclow base then print name 
        if(score == secscore):
            print(name)
            #break
            # keep looking, just don't print matching dupe names
        m = m + 1

    