
def solution(numbers):
    answer=""
    compare = []
    for number in numbers:
        temp = (str(number)*4)[0:4]
        compare.append([temp,str(number)])
    compare.sort(reverse =True)
    for  c in compare:
        answer+=c[1]
    if answer[0]=='0':
        answer='0'
    return answer

print (solution([90,908,89,898,10,101,1,8,9]))
    ##

    # 3 30 34 5 52 9
    #=>  9 5 52 34 3 30