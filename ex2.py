with open('ledger.txt', 'r', encoding='utf-8') as file:
    context = list(map(str.strip, file.readlines()))
    print(''.join(('$', str(sum(map(lambda x:int(x[1:]), context))))))