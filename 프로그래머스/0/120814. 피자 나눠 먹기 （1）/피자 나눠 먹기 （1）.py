def solution(n):
    answer = 0
    if n <= 7:
        answer = 1
    else:
        if n % 7 == 0:
            answer = (n // 7)
        else:    
            answer = 1 + (n // 7)
    return answer