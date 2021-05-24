from typing import DefaultDict


def solution(n):
    answer = 0
    binstr = format(n,'b')
    strlen = len(binstr)
    index =0
    for i in range(strlen-1,-1,-1):
        flag =0
        if binstr[i]=='1':
            for j in range(i-1,-1,-1):
                if binstr[j]=='0':
                    #binstr[j]='1'
                    #binstr[i]='0'
                    binstr = binstr[0:j]+'1'+binstr[j+1:i]+'0'+binstr[i+1:]
                    flag =1
                    index = j
                    break
            else:
                index = 0
                binstr ='10'+binstr[1:]
                flag = 1
                break

        if flag==1:
            break
    
    right =binstr[index+1: ]
    counter =0

    for i in range(len(right)):
        if right[i]=='1':
            counter+=1
    temp=''
    for i in range(len(right)-counter):
        temp+='0'
    for i in range(counter):
        temp+='1'
    binstr = binstr[:index+1]+temp
    answer = int(binstr,2)
    return answer
    

solution(15)

# 6 = 110 => 1010=>1001
# 15 = 1111 => 10111
# ? = 1010000 => 1000001 
# ? = 1010001 => 10