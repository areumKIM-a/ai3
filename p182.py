# list1=[3,15,-12.5,'사과','딸기',True,False] #[3, 15, -12.5, '사과', '딸기', True, False]
# list2=list(range(1,21,2)) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# print(list1)
# print(list2)
# for i in range(7):
#    print(list1[6-i],end=" ") #False True 딸기 사과 -12.5 15 3
# print()
# print("-"*50)
# print(list2[-4:]) #[13, 15, 17, 19]
# print()
# print("-"*50)
# print(list2[::2]) #[1, 5, 9, 13, 17]
# print(list2[-1::-2]) #[19, 15, 11, 7, 3]

# #100 110 120 ....200 리스트
# list3=list(range(100,201,10))
# for i in list3:
#    print(i,end=" ")
# print()
# #갯수
# cnt=0
# for i in list3:
#    cnt=cnt+1
# print("리스트의 갯수는 %d"%cnt)
# #합계를 구하기
# sum=0
# for i in list3:
#    sum=sum+i
# print("리스트의 합계는 %d"%sum)
# print(len(list3)) # 리스트의 갯수 구하기

# #p185
# colors=['빨간색', '파란색','노란색','검정색','초록색']
# for i in colors:
#   print("나는 %s을 좋아한다"%i)
# print("-"*30)
# n=len(colors)
# for i in range(0,n):
#    print("나는 %s을 좋아한다"%colors[i])
# print("-"*30)
# animals=['코끼리','호랑이','사슴','펭귄','여우']
# i=0
# while i<len(animals):
#    print(animals[i])
#    i=i+1

#성적 프로그램 작성하기
# list1=['홍길동',50,80]
# list2=['이순신',90,75]
# list3=['최경미',100,100]
# print("이름 국어점수 수학점수 합계 평균")
# for i in list1:
#     print(i,end=" ")
# print()
# for i in list2:
#     print(i,end=" ")
# print()
# for i in list3:
#     print(i,end=" ")
# print()
# print(list1[0],list1[1],list1[2],list1[1]+list1[2],(list1[1]+list1[2])/2)
# print(list2[0],list2[1],list2[2],list2[1]+list2[2],(list2[1]+list2[2])/2)

# #이름만
# print("우리반 이름:",list1[0],list2[0],list3[0])
# print("우리반 이름: %s %s %s"%(list1[0],list2[0],list3[0]))
# print("우리반 국어점수 합계: %s"%(list1[1]+list2[1]+list3[1]))
# print("우리반 영어점수 합계: %s"%(list1[2]+list2[2]+list3[2]))


# '''if int(list2[1])<int(list1[1]) and int(list3[1])<int(list1[1]):
#     print(topKorName=list1 %s"%list1[0])
# elif int(list1[1])<int(list2[1]) and int(list3[1])<int(list2[1]):
#     print("우리반에서 국어 1등은: %s"%list2[0])
# else:
#     print("우리반에서 국어 1등은: %s"%list3[0])'''
# if list2[1]<list1[1] and list3[1]<list1[1]:
#     topKorName=list1
# elif list1[1]<list2[1] and list3[1]<list2[1]:
#     topKorName=list2
# else:
#     topKorName=list3
# print("우리반에서 국어 1등은: %s"%topKorName[0])

# findName=input("찾고 싶은 사람은? ")
# if findName==list1[0] or findName==list2[0] or findName==list3[0]:
#     print("우리반에 %s 있어요"%findName)
# else:
#     print("우리반에 %s 없어요"%findName)


