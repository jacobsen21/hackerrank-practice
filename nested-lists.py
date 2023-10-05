if __name__ == '__main__':

    # records = []

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    #     records.append([name, score])

    # debug 
    records = [['first', 11.11], ['third', 33.33], ['second', 22.22]]
    print(records)

    # sort / reverse 
    print(records.sort())
    
    # nested for loop to access each name/value pair
    for student in records:
        for score in student:
            print(score)