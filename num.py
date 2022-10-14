NUM = {'IV': 4, 'IX': 9, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
       'M': 1000, 'I': 1, 'V': 5,
       }

def solution(roman):
    res = ''
    lst = []
    while roman:
        if roman[:2] in NUM.keys():
            res += str(NUM[roman[:2]])
            roman = roman[2:]
        else:
            lst.append(NUM[roman[:1]])
            roman = roman[1:]
    return res + str(sum(lst))






print(solution('IVCIX'))



# def solution(roman):
#     res = 0
#     for key, value in NUM.items():
#         while key in roman:
#             ind = roman.find(key)
#             roman = roman[:ind] + roman[ind+len(key):]
#             res += value
#     return res