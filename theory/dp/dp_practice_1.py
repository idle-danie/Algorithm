## 1만들기

def test1(x):
    d = [0] * 10000
    for i in range(2, x+1):
        d[i] = d[i-1] + 1
        if i%5==0:
            d[i] = min(d[i], d[i//5] + 1)
        elif i%3==0:
            d[i] = min(d[i], d[i//3] + 1)
        elif i%2==0:
            d[i] = min(d[i], d[i//2] + 1)
    return d[x]

def test2(x):
    d = [0] * 10000
    for i in range(2, x+1):
        d[i] = d[i-1] + 1
        if i%5==0:
            d[i] = min(d[i], d[i//5] + 1)
        if i%3==0:
            d[i] = min(d[i], d[i//3] + 1)
        if i%2==0:
            d[i] = min(d[i], d[i//2] + 1)
    return d[x]

for i in range(1,200):
    if test1(i) != test2(i):
        print("{} {} {}".format(i, test1(i), test2(i)))
