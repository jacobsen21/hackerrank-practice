if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}

    # debug remove
    # n = 3
    # student_marks = {'Krishna': [45.0, 56.0, 67.0], 
    #                  'Arjun': [34.0, 23.0, 78.0], 
    #                  'Malika':[52.0,56.0, 60.0]}
    
    n = 2
    student_marks = {'Harsh': [25, 26.5, 28], 
                     'Arjun': [34.0, 23.0, 78.0]}

    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    
    # query_name = input()

    # debug remove
    # query_name = 'Malika'
    query_name = 'Harsh'

    # print(n,student_marks, query_name)
    # print(student_marks['you'])

    total = 0.00
    avg = 0.00

    for i in student_marks[query_name]:
        total += i

        # debug remove
        # print(i)

    avg = total / 3
    # debug remove
    # print(total)

    print(f'{avg:.2f}')