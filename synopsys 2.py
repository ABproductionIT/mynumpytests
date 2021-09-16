# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
# def solution(S):
#     # write your code in Python 3.6
#     numberlist = []
#     pricelist = []
#     user = S.split("\n")
#     for i in range(len(user)):
#         usdata = user[i].split(',')
#         x = usdata[0]
#         numb = usdata[1].split('-')
#         map_numb = map(int, numb)
#         numb_sum = sum(list(map_numb))
#         h, m, s = x.split(':')
#         sec = int(h) * 3600 + int(m) * 60 + int(s)
#         if sec < 300:
#             price = sec*3
#             pricelist.append(price)
#             numberlist.append(numb_sum)
#         elif sec == 300:
#             price = int(sec/60)*150
#             pricelist.append(price)
#             numberlist.append(numb_sum)
#         elif sec > 300:
#             price = (int(m)+1) * 150
#             pricelist.append(price)
#             numberlist.append(numb_sum)
#     return pricelist, numberlist
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    numberlist = []
    pricelist = []
    user = S.split("\n")
    for i in range(len(user)):
        usdata = user[i].split(',')
        x = usdata[0]
        numb = usdata[1].split('-')
        map_numb = map(int, numb)
        numb_sum = sum(list(map_numb))
        h, m, s = x.split(':')
        sec = int(h) * 3600 + int(m) * 60 + int(s)
        if sec < 300:
            price = sec*3
            pricelist.append(price)
            numberlist.append(numb_sum)
        elif sec == 300:
            price = int(sec/60)*150
            pricelist.append(price)
            numberlist.append(numb_sum)
        elif sec > 300:
            price = (int(m)+1) * 150
            pricelist.append(price)
            numberlist.append(numb_sum)

    return max(pricelist)




# print(solution("00:01:07,400-234-090"))

print(solution("""00:01:07,400-234-090
00:05:01,701-080-080
00:05:00,400-234-090"""))
