def solution(str1, str2):
    answer = 0
    _str1=''
    _str2=''
    
    a={}
    b={}

    _str1 =str1.lower()
    _str2 =str2.lower()
    
    
    for i in range(len(_str1)-1):
        
        if _str1[i].isalpha() and _str1[i+1].isalpha():
            if a.get(_str1[i]+_str1[i+1]) is None:
                a[_str1[i]+_str1[i+1]] = 1
            else:
                a[_str1[i]+_str1[i+1]]=a[_str1[i]+_str1[i+1]]+1

    for i in range(len(_str2)-1):
        if _str2[i].isalpha() and _str2[i+1].isalpha():
            if b.get(_str2[i]+_str2[i+1]) is None:
                b[_str2[i]+_str2[i+1]] = 1
            else:
                b[_str2[i]+_str2[i+1]]=b[_str2[i]+_str2[i+1]]+1

    same =0
    total=0
    for i in a:
        if b.get(i) is not None:
            if a[i]>b.get(i):
                same+=b.get(i)
            else:
                same+=a.get(i)
        total+=a[i]
    for i in b:
        total+= b[i]
    
    if total ==same:
        answer = 65536
    else:
        answer=int((same/(total-same))*65536)

    return answer


solution("AB","shake hands")