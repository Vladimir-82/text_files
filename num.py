f = open('numbers.txt', 'r', encoding='utf-8')
content = f.readlines()
for i in content:
    print(sum([int(j) for j in i.rstrip().split()]))





with open('numbers.txt', 'r', encoding='utf-8') as file:
    context = list(map(str.strip, file.readlines()))
    for i in context:
        print(sum(map(int, i.split())))