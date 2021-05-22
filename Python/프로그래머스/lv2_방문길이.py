def solution(dirs):
    answer = 0
    x=0 
    y=0
    road =[]
    for dir in dirs:
        
        if dir =='U':
            if y+1<=5:
                if(x,y,x,y+1) not in road:
                    road.append((x,y,x,y+1))
                    road.append((x,y+1,x,y))
                
                y=y+1
        elif dir =='L':
            if x-1>=-5:
                if(x,y,x-1,y) not in road:
                    road.append((x,y,x-1,y))
                    road.append((x-1,y,x,y))
                x=x-1
        elif dir =='R':
            if x+1<=5:
                if(x,y,x+1,y) not in road:
                    road.append((x,y,x+1,y))
                    road.append((x+1,y,x,y))
                x=x+1
        elif dir=='D':
            if y-1>=-5:
                if(x,y,x,y-1) not in road:
                    road.append((x,y,x,y-1))
                    road.append((x,y-1,x,y))
                y=y-1
    answer=len(road)//2


    return answer

solution("LULLLLLLU")