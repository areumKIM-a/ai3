#정렬
'''data=[12,8,15,32,-3,-20,15,34,6]
print(data)
data.sort()
print(data)

data2=['a','가','@','1','ac']
print(data2)
data2.sort()#오름차순 유니코드 순서대로
print(data2)
#내림차순 정렬
data2.sort(reverse=True)#내림차순
print(data2)
data2.sort(reverse=False)#오름차순
print(data2)

#p205
string1=('사과는 맛있다. 나는 사과를 좋아한다. 사과')
print(string1)
i=string1.replace('사과','딸기',-1)
print(i)
print()
string1=['사과는 맛있다. 나는 사과를 좋아한다. 사과']
print(string1)
x=string1[0].replace('사과','딸기',-1)
string1=[x]
print(string1)'''

#p207 문자열 쪼개기 split()
'''hello='have a nice day'
print(hello)

list1=hello.split(" ")
print(list1)
print(type(list1))

for i in range(0,len(list1)):
    print("list1[%d]:%s"%(i,list1[i]))

list1='a,b,c,d,e,f'
print(list1)
list1Sp=list1.split(",")
print(list1Sp)
print(type(list1Sp))

for i in range(0,len(list1Sp)):
    print("list1Sp[%d]:%s"%(i,list1Sp[i]))
print()
list2=['홍길동:100:20','이순신:90:80','최수연:100:75']
#출력형식 list2[0]=['홍길동:100:20']
#list22[0]=['홍길동']
#list22[1]=['100']
list22=[]
print(list22)
for i in list2:
    list10=i.split(':')
    print(list10)
    for j in list10:
        list22.append(j)
print(list22)'''

'''list5=['kbs-사장-200,mbc-부장-100','kbs-사원-50, sbs-대리-80']
list_5=[]
for i in list5:
    list50=i.split('-')
    print(list50)
    for j in list50:
        list55=j.split(',')
        print(list55)
        for k in list55:
            list_5.append(k)
            print(list_5)
print(list_5)'''

'''import requests as req
url="https://search.naver.com/search.naver"
rData=req.get(url,params={'query':'백일해증상'})
print(rData.text)'''

#p212
'''list2D=[[1,2],[3,4,5],[1]]
print(list2D[1][1])#4
print(list2D[0][1])#2
print()
list2DD=[[1,2,3,4],[5,6,7]]
print(list2DD[1][0],end=" ")
print(list2DD[1][1],end=" ")
print(list2DD[1][2],end=" ")
print()

print(len(list2DD))
print(len(list2DD[0]))
print(len(list2DD[1]))

for i in range(0,len(list2DD)):
    for j in range(0,len(list2DD[i])):
        print(list2DD[i][j],end=" ")
    print()

list3D=[[[1,2,3],[4,5]],[[6,7],[8]]]
#8을 출력
print(list3D[1][1][0])
#1을 출력
print(list3D[0][0][0])

#218~222
#C5-5
questions=['s_hool','compu_er','deco_ation','windo_','hi_tory']
answers=['c','t','r','w','s']
for i in range(len(questions)):
    q="%s : 밑 줄에 들어갈 알파벳은? "%questions[i]
    guess=input(q)

    if guess==answers[i]:
        print('정답!')
    else:
        print('틀렸어요!')

#C5-8
seats=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0],[0,1,0,0,0,1,0,1,0,0],[0,0,0,0,0,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,1]]

for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j]==0:
            print("%3s"%"□",end="")
        else:
            print("%3s"%"■",end="")
    print()'''

scores=[]

while True:
    x=int(input('성적을 입력하세요(종료 시 -1 입력): '))
    if x==-1:
        break
    else:
        scores.append(x)
sum=0
for k in scores:
    sum=sum+k
avg=sum/len(scores)
print("합계: %d, 평균: %.2f"%(sum,avg))



