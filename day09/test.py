# 타겟넘버
def solution(numbers, target):
    answer = 0
    
    def mini_solution(index, result_sum):
        nonlocal answer
        if index == len(numbers):
            if target == result_sum:
                answer+=1
            return
        mini_solution(index+1, result_sum+numbers[index])
        mini_solution(index+1, result_sum-numbers[index])
    mini_solution(0,0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))