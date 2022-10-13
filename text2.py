f = open('prices.txt', 'r', encoding='utf-8')
content = f.readlines()
[print(i.rstrip()) for i in reversed(content)]
f.close()