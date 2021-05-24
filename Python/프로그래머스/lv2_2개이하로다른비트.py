def solution(numbers):
    answer=[]
    for number in numbers:
        num_str = format(number,'b')
        num_len = len(num_str)
        left=""
        right=""
        final=""
        for i in range(num_len-1,-1,-1):
            if num_str[i]=='0':
                left = num_str[:i]+'1'
                right =num_str[i+1:]
                break
        else:
            left = '1'
            right='0'+num_str[1:]
            final = left+right
            answer.append(int(final,2))
            continue

        for i in range(len(right)):
            if right[i]=='1':
                right = right[:i]+'0'+right[i+1:]
                break
        
        final = left+right
        answer.append(int(final,2))

    return answer

print(solution([2,3,4,5,6,7,8]))

# 10111111 =>11111100
# 10101 =>  1011 1 
# 11000000
