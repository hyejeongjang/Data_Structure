def solution(x):
    answer = 0
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        return solution(x-1)+solution(x-2)
print(solution(10))
