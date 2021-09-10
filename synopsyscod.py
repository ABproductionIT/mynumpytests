# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def calcu(x, y):
    for s in range(len(x) - 1):
        if x[s] == max(x):
            return y[s]


def solution(T):
    # write your code in Python 3.6
    summer = []
    winter = []
    spring = []
    autumn = []
    period = len(T) / 4
    year = len(T)
    for i in range(year):
        if i >= 0 and i < period:
            winter.append(int(T[i]))
        elif i >= period and i< (period * 2):
            spring.append(int(T[i]))
        elif i >= (period * 2) and i < (period * 3):
            summer.append(int(T[i]))
        else:
            autumn.append(int(T[i]))

    eqwint = max(winter) - min(winter)
    eqspr = max(spring) - min(spring)
    eqsum = max(summer) - min(summer)
    eqaut = max(autumn) - min(autumn)

    calc = [eqwint, eqspr, eqsum, eqaut]
    seasons = ["WINTER", "SPRING", "SUMMER", "AUTUMN"]
    for s in range(4):
        if calc[s] == max(calc):
            return seasons[s]







print(solution([2, 1, 1, 10, 2, 13, 3, -18]))
