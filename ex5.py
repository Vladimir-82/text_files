# name = input()
# # f = open('prices.txt', 'r', encoding='utf-8')
# f = open(name, 'r', encoding='utf-8')
# content = list(map(str.strip, f.readlines()))[-10:]
# [print(i) for i in content]


with open(input()) as file:
    print(*file.readlines()[-10:], sep='')