if __name__ == '__main__':

    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])

    n = len(records)

    # debug - hidden test case #2
    # input:
    # n = 5
    # records = [['Harsh', 20], ['Beria', 20], ['Varum', 19], 
    #            ['Kakunami', 19], ['Vikas',21]]
    # expected output: 
    # Beria
    # Harsh
    
    # debug - hidden test case #3
    # n = 4
    # records = [['Rachel', -50], ['Mawer', -50], ['Sheen', -50], 
    #            ['Shaheen', 51]]
    # # expected output:
    #  Shaheen



    # initial alpha sort to get names in alpha order
    records.sort()

    # sort by scores - x[element 0 or 1]
    records.sort(key=lambda x : x[1])
    
    # set lowest name and score
    lowestname, lowestscore = records[0]
   
    m=1
    while m < n:

        # set individual name and score elements 
        # from current list
        name, score = records[m]  
        # determine prev name and score as well
        prevname, prevscore = records[m-1]
  
        # look for secondlowest starting score - break out
        # of loop 
        if(score > prevscore):
            secondlowestscore = score
            break


        m = m + 1

    # print(secondlowestscore)

    # reset while loop counter and select all score that match
    # secondlowest score
    m=0
    while m < n:
        secname, secscore = records[m]
        if(secscore == secondlowestscore):
            print(secname)

        m = m + 1   