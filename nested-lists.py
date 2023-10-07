if __name__ == '__main__':

    # records = []

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    #     records.append([name, score])

    # sort by name function
    def sortbyvalue(records):
        return(sorted(records, key=lambda x: x[1], reverse=False))
        
    # debug 
    n = 3
    records = [['first', 53.21], ['third', 3.33], ['second', 232.22]]
    print(records)

    # min/max
    # print("max: ", max(records))
    # print("min: ", min(records))
    # print("first in list: ", records[0])

    # initial alpha sort
    records.sort()
    print(records)

    # newlist = sort(records[1])
    # print(newlist)

    # sortbyvalue(records)
    # print(records)


    # sort / reverse 
    # print("reverse sorted: ", records.sort(reverse=True))
    # print("second to worst score: ", records[n-2])
    
    # nested for loop to access each name/value pair
    # for student, score in records: 
    #     print(student)
    #     for score in student:
    #         print(score)

    # determine how to sort values 
    # then select idx 1 and check if idx1 + 1 is equal 
    # do not exceed n entries
    