f = open('prices.txt', 'r', encoding='utf-8')
content = f.readlines()
print(sum(map(lambda x: int(x[1]) * int(x[2]), map(lambda y: y.rstrip().split('\t'), content))))
f.close()
