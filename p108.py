#배수

# result="3의 배수도 4의 배수도 아니다"
# if num%3==0:
#     result="3의 배수이다"
# if num%4==0:
#     result="4의 배수이다"
# if num%3==0 and num%4==0:
#     result="3의 배수이면서 4의 배수이다"

# print("%d는 %s"%(num,result))

# num=int(input("숫자를 입력하세요: "))
# result=num
# if num%2==0 and num%4==0:
#     result="행운의 수"
# if num==4:
#     result="행운의 수"
# if num==8:
#     result="행운의 수"
   
# print("%d는 %s"%(num,result))

#영어단어
# ans1=input('"사자"의 영어단어는 무엇일까요?: ')
# result="땡! 틀렸습니다"
# if ans1=="lion":
#     result="딩동댕! 참 잘했어요~~~"
# else: 
#     print(result)

#C3-1
'''startNum=int(input("시작 수는? "))
endNum=int(input("끝 수는? "))
jungsu=int(input("정수를 입력하세요: "))
result="%d는 %d~ %d사이에 없다"%(jungsu,startNum,endNum)
if jungsu >= startNum and jungsu<=endNum :
    result="%d는 %d~ %d사이에 있다"%(jungsu,startNum,endNum)
print(result)'''

'''month=int(input("월을 숫자로 입력하세요: "))
if month>=3 and month<=5:
    print("%d는 봄입니다"%month)
if month>=6 and month<=8:
    print("%d는 여름입니다"%month)
if month>=9 and month<=11:
    print("%d는 가을입니다"%month) 
if month==2 or month==1 or month==12:
    print("%d는 겨울입니다"%month) '''

a=input("주민번호 뒷자리 첫 번째 숫자를 입력해 주세요")
if a=="1" or a=="3":
    print("남자입니다")
if a=="2" or a=="4":
    print("여자입니다")
else :
    print("정확한 숫자를 입력해 주세요")
