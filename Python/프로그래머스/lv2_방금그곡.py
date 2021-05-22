def solution(m, musicinfos):
    answer = ''
    museinfo=[]
    print(m)
    for musicinfo in musicinfos:
        tokens = musicinfo.split(",")
        start = tokens[0]
        end = tokens[1]
        title=tokens[2]
        muse = tokens[3]
        total_time=(int(end[:2])-int(start[:2]))*60+int(end[3:5])-int(start[3:5])
        muses=[]
        final_sheet=""
        for mu in muse:
            if mu=='#':
                muses[-1]+='#'
            else:
                muses.append(mu)
        
        if total_time<=len(muses):
            for i in range(total_time):
                final_sheet+=muses[i]
        else:
            counter=0
            while counter<total_time:
                final_sheet+=muses[counter%len(muses)]
                counter+=1
        print(total_time,len(muses))
        print(muses,final_sheet)
       
        _museinfo=[total_time,int(start[:2])*60+int(start[3:5]),title]
        
        
        for i in range(len(final_sheet)-len(m)+1):
            #       0123456789 01234567 = len =18
            #       12345              = len = 5
            #     i=0~12 =18-5-1
            if m[0]==final_sheet[i]:
                
                if m == final_sheet[i:len(m)+i] :
                    #  '#'이 len(m)+i 에 있는지 체크
                    #  final_sheet= 0~len(final_sheet)-1
                    if len(m)+i<=len(final_sheet)-1:
                        if  final_sheet[len(m)+i]!='#':
                            if museinfo:
                                if _museinfo[0]>museinfo[0]:
                                    museinfo=_museinfo
                                elif _museinfo[0]==museinfo[0]:
                                    if _museinfo[1] < museinfo[1]:
                                        museinfo=_museinfo
                            else:
                                museinfo=_museinfo
                    
                    else:
                        if museinfo:
                            if _museinfo[0]>museinfo[0]:
                                museinfo=_museinfo
                            elif _museinfo[0]==museinfo[0]:
                                if _museinfo[1] < museinfo[1]:
                                    museinfo=_museinfo
                        else:
                            museinfo=_museinfo

    if museinfo:
        return museinfo[2]
    else:
        return "(None)"
    

solution("ABC",["12:00,12:06,HELLO,A#BCC#D#E#", "13:00,13:07,WORLD,ABCDEF"])