def solution(numbers,k):
    answer=''
    start = 0
    for i in range(k):
        if numbers[start]=='9':
            start +=1
        
        for j in range(start, len(numbers)-1):
            if numbers[j]<numbers[j+1]:
                numbers = numbers[0:j]+numbers[j+1:]
                break
        else:
            if numbers[-1]>numbers[-2]:
                numbers=numbers[0:-2]+numbers[-1]
            else:
                numbers = numbers[0:-1]
        
    answer = numbers
    return answer
