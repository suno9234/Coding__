def solution(n, arr1, arr2):
    answer = ['' for i in range(n)]
    for i in range(n):
        arr1tobin = format(arr1[i],'b')
        arr2tobin = format(arr2[i],'b')

        zeros1 = n-len(arr1tobin)
        zeros2 = n-len(arr2tobin)

        if zeros1>0:
            for j in range(zeros1):
                arr1tobin = '0'+arr1tobin
        if zeros2>0:
            for j in range(zeros2):
                arr2tobin = '0'+arr2tobin

        
        
        for j in range(n):
            if arr1tobin[j] =='1' or arr2tobin[j]=='1':
                answer[i] += '#'
            else:
                answer[i] +=' '
        
    return answer
