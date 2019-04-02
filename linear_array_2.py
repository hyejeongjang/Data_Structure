L = [64, 72, 83, 72, 54]
x = 72
def solution(L, x):
    answer=[]
    if x not in L:
        answer.append(-1)
    else:
        for i in range(len(L)):
            if x==L[i]:
                answer.append(i)
    return answer
print(solution(L, x))
