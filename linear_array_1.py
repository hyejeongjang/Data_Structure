L = [20, 37, 58, 72, 91]
x = 65
def solution(L, x):
    answer=[]
    length=len(L)
    if(L[0]>x):
        L.insert(0, x)
    if(L[length-1]<x):
        L.insert(length-1, x)
    for i in range(length):
        max=L[0]
        if(L[i]<x) and (L[i+1]>x):
            L.insert(i+1, x)
    answer=L
    return answer
print(solution(L, x))
