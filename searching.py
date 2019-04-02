L = [64, 72, 83, 72, 54]
x = 72
def solution(L, x):
    if x in L:
        return L.index(x)
    else:
        return -1
print(solution(L, x))
