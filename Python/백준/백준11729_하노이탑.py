

def hanoi(height,xNow,xFuture) :
    myset ={1,2,3}
    set1 = {xNow,xFuture}

    arr = list(set(myset)-set(set1))

    if height == 1:
        print(xNow,xFuture)
        return
    
    hanoi(height-1,xNow,arr[0])

    print(xNow,xFuture)

    hanoi(height-1,arr[0],xFuture)

    return


k = int(input())

print(2**k-1)
hanoi(k,1,3)

