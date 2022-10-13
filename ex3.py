with open('grades.txt', 'r', encoding='utf-8') as file:
    count = 0
    context = list(map(str.strip, file.readlines()))
    for i in context:
        res = filter(lambda x: int(x) > 64, i.split()[1:])
        # print(list(res))
        if len(list(res)) == 3:
            count += 1
print(count)
