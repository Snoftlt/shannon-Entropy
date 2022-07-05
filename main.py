import copy
def sigma(firstArr):
    sigma = []
    for j in range(len(firstArr[0])):
        sigma.append(0)
        for i in range(len(firstArr)):
            sigma[j] += firstArr[i][j]
    return sigma
def normalize(firstArr, normalizedArr):
    normalizedArr = copy.deepcopy(firstArr)
    sigma = sigma(firstArr)
    for j in range(len(normalizedArr[0])):
        for i in range(len(normalizedArr)):
            normalizedArr[i][j] = normalizedArr[i][j]/sigma[j]
def SE(normalizedArr):
    SE = []
    for j in range(len(normalizedArr[0])):
        SE.append(0)
        h2 = 0
        h1 = (-1/math.log(len(normalizedArr)))
        for i in range(len(normalizedArr)):
            h2 += (normalizedArr[i][j]*math.log(normalizedArr[i][j]))
        SE[j] = h1*h2
    return SE
def dj(SE):
    d = [(1-SE[j]) for j in range(len(SE))]
    return d
def Wj(d):
    sigma = 0
    for j in range(len(d)):
        sigma += d[j]
    W = [(d[j]/sigma) for j in range(len(d))]
    return W
def Xi(normalizedArr, W):
    X = [0 for i in range(len(normalizedArr))]
    for i in range(len(normalizedArr)):
        for j in range(len(normalizedArr[0])):
            X[i] += (normalizedArr[i][j]*W[j])
    return X
def floatArr(firstArr):
    for i in range(len(firstArr)):
        for j in range(len(firstArr[0])):
            firstArr[i][j] = float(firstArr[i][j])
path = input()
firstArr = []
with open(path, "r") as f:
    for i in f:
        firstArr.append(i.replace(",", " ").split())
    floatArr(firstArr)
normalize(firstArr, normalizedArr)
s = SE(normalizedArr)
d = dj(s)
w = Wj(d)
x = Xi(normalizedArr, w)
print("Shannon Entropy Point index is {i}".format(i = (x.index(max(x))+1)))
print("Shannon Entropy Point is {i}".format(i = firstArr[x.index(max(x))]))
