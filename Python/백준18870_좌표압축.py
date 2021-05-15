n = int(input())

x =[]
x = input().split()
x = list(map(int,x))

original = x.copy()

x = list(set(x))
x.sort()

mydict = dict()

mylen = len(x)

for i in range(0,mylen):
    mydict[x[i]] = i
    
for i in original : 
    print(str(mydict.get(i))+" ",end='')



