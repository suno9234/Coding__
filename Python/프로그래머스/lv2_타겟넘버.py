

answer=0

def solution(numbers, target):
    operator=[False for i in range(len(numbers))]
    func(0,numbers,operator,target)
    global answer
    return answer

def func(counter,numbers,operator,target):
    global answer
    if counter == len(numbers):
        temp =0
        for i in range(len(numbers)):
            if operator[i]:
                temp+=numbers[i]
            else:
                temp-=numbers[i]
        
        if temp == target:
            answer=answer+1
        return
    
    
    
    operator[counter]=True
    func(counter+1,numbers,operator,target)
    operator[counter]=False
    func(counter+1,numbers,operator,target)
        
    

