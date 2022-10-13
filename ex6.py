result = []
with open(input(), 'r', encoding='utf-8') as file, \
        open('forbidden_words.txt', 'r', encoding='utf-8') as forb:
    text = list(map(str.strip, file.readlines()))
    forbiden = forb.read().split()
    for i in text:
        string = i
        for j in forbiden:
            while j in string.lower():
                index = string.lower().find(j)
                string = string[:index] + '*' * len(j) + string[index+len(j):]
        result.append(string)
[print(i) for i in result]


