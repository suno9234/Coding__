mylist = []

#list의 가장 끝에 새 원소를 집어넣음
mylist.append(1)
mylist.append(2)
mylist.append(1)
mylist.append(3)

print(mylist)
#[1, 2, 1, 3]

mylist.insert(2,1)
#mylist[2]에 1의 값을 집어넣음
print(mylist)
#[1, 2, 1, 1, 3]

mylist.remove(1)
#가장 처음 만나는 1이 지워짐
print(mylist)
#[2, 1, 1, 3]

print(mylist.pop())
#가장 끝의 원소를 반환하고 제거함 => list를 스택으로 사용할 수 있음
# 3
print(mylist)
#[2, 1, 1]

del mylist[0]
# index에 있는 원소를 제거함
print(mylist)
#[1, 1]

mylist2 = [5,3,1,2,4]

mylist2.reverse()
#뒤집기 [4, 2, 1, 3, 5]

mylist2.sort()
# 오름차순 정렬
# 1,2,3,4,5

print(len(mylist2))
#list의 길이 구하기
# 5

mylist3 = list(range(0,10))
# range를 이용하여 list 만들기
print(mylist3)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

####### range(start , end , 증가폭)
####### (i = start ; i <end ; i=i+증가폭)

print(min(mylist3)) # 최소 0
print(max(mylist3)) # 최대 9 
print(sum(mylist3)) # 합  45

# list안에 for문으로 리스트 생성하기

squares = [value**2 for value in range(1,10)]
print(squares)

#  list 자르기
temp = squares[1:3]
print(temp)

temp = squares[:10:2]
print(temp)

# list 는 '=' 로 복사하면 주소값 복사됨
# 따라서 [ : ] 사용하거나 copy() 사용

newlist = temp[ : ]
newlist2 = temp.copy()
newlist[3] = -1
newlist2[2]=-1

print(newlist)
print(newlist2)
print(temp) 