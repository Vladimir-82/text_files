with open('words.txt', 'r', encoding='utf-8') as file:
    context = file.read()
    maximum = len(sorted(context.split(), key=len)[-1])
    [print(i) for i in context.split() if len(i) == maximum]