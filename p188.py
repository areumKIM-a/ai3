'''nameList=['a','b']
noList=list(range(241001,241021))
print(noList)
print(nameList[1])
for i in noList:
    print(i,end=" ")

print()
i=0 #20
while i <len(noList):
    print(noList[i],end=" ")
    i=i+1'''

'''nameList=['이순신','홍길동','박수연']
#박수연을 박수현으로 바꾸기
nameList[2]='박수현'
for i in nameList:
    print(i,end=" ")
print()

#정현희를 추가하기
nameList.append('정현희')
for i in nameList:
    print(i,end=" ")

#이순신 이승후 홍길동 박수현 정현희  이승후 삽입하기
nameList.insert(1,'이승후')
print()
for i in nameList:
    print(i,end=" ")
print()'''

#이순신 이승후 홍길동 박수현 정현희
#문제 박수현은 몇번째 인덱스에?
try:
    nameList=['박수현','이순신', '이승후', '홍길동', '박수현', '정현희']
    searchIndex=nameList.index('장수현',1,10)
    print(searchIndex)
except ValueError:
    print('장수현은 리스트에 없습니다')

#p194
'''member=[1,2,3,2,2,2,4]
member.remove(2) #첫번째 값2가 삭제
print(member)

member=[1,2,3,4,2,2,2]
member.pop(2) #2번 인덱스를 삭제
print(member)
member.clear()
print(member)'''

#p199
p1=[1,2,3,4,5]
p2=[6,7,8,9,10]
p3=p1+p2
print(p3)

#p200
p4=list(range(1,11)) 
print(p4)
p4Sum=sum(p4)
print(p4Sum)

'''sum=0
for i in p4:
    sum=sum+i
print(sum)'''

p5=[100,8,90]
p5Sum=sum(p5)
print(p5Sum)
p5Avg=p5Sum/len(p5)
print(p5Avg)
p5Max=max(p5)
print(p5Max)
p5Min=min(p5)
print(p5Min)

p5.reverse()
print(p5)
p5.reverse()
print(p5)

p6=['apple','banana','orange']
p6Copy=p6.copy()
print(p6Copy)

#apple을 지우세요
p6.remove('apple')
print(p6)
print(p6Copy)
#p6Copy에 오렌지를 망고로 바꾸기
p6Copy[2]='mango'
print(p6)
print(p6Copy)
print()
p7=['apple','banana','orange']
p77=p7
print(p7)
print(p77)
print()

#p7에  있는 애플을 삭제
#p77에 있는 오렌지를 망고로 변경하기
#p7에 'bear' 추가하기
p7Copy=p7.copy()
p7.remove('apple')
print(p7)
print(p77)
print(p7Copy)
p77[1]='mango'
print(p7)
print(p77)
print(p7Copy)
p7.append('bear')
print(p7)
print(p77)
print(p7Copy)
