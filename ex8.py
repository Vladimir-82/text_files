res = []
with open(input(), 'r', encoding='utf-8') as file:
    data = list(map(str.strip, file.readlines()))
    for i, string in enumerate(data):
        if 'def ' in string:
            if not '#' in data[i - 1]:
                ind = string.find('(')
                res.append(string[4:ind])
if not res:
    print('Best Programming Team')
else:
    [print(i) for i in res]

