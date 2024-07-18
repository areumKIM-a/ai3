'''year=2024
month="07"
day=15
print(year, month, day, sep="-")'''

'''price=1000
print(price,"원",sep="")'''

'''print("안녕하세요\n반갑습니다")
print("안녕하세요\t반갑습니다")
print("\\")
print("\'안녕\'")
print("\"반갑습니다\"")
print("안녕하세요\\반갑습니다")'''

'''#퀴즈
kor=input("국어 성적을 입력하세요:")
eng=input("영어 성적을 입력하세요:")
math=input("수학 성적을 입력하세요:")
sum=int(kor)+int(eng)+int(math)
avg=sum/3
print("합계:%d, 평균:%.2f"%(sum,avg))'''

#C2-1
'''year=input("년은?")
month=input("월은?")
day=input("일은?")
print(year,month,day,sep=".")'''

#C2-2
'''width=int(input("사각형의 너비는?"))
height=int(input(" 사각형의 높이는?"))
girth=2*width+2*height
area=width*height
print("사각형의 너비: %dcm"%width)
print("사각형의 높이: %dcm"%height)
print("둘레길이: %dcm"%girth)
print("면적: %d㎠"%area)'''

#C2-3
'''r=float(input("반지름은?"))
length=2*r*3.14
area=r*r*3.14
print("반지름: %.2fcm"%r)
print("원의 둘레: %.2fcm"%length)
print("원의 면적: %.2f㎠"%area)'''

#C2-4
'''inch=float(input("인치는?"))
cm=inch*2.54
print("%.1f inch=>%.1f cm"%(inch,cm))'''

#C2-5
'''bookPrice=int(input("책 값은? "))
discount=int(input("할인율은? "))
delivery=int(input("배송료는? "))
pay=bookPrice-(bookPrice*(discount/100))+delivery
print("책 값: %d원"%bookPrice)
print("할인율: %d"%discount)
print("배송료: %d원"%delivery)
print("결제 금액: %d원"%pay)'''

#E2-1
a=10
b=20
c=(int(a)+int(b))
print(c)

#E2-2
print("%d+%d=%d"%(a,b,c))
#E2-3
print(str(a)+'+'+str(b)+'='+str(c))
#E2-4
frute1=input("첫 번째 과일을 입력하세요: ")
frute2=input("두 번째 과일을 입력하세요: ")

#E2-4,5
print(frute1,"와",frute2,"은 내가 좋아하는 과일이다.")
print(frute1,"와 ",frute2,"은 내가 좋아하는 과일이다.",sep="")
#E2-6
print("%s와 %s은 내가 좋아하는 과일이다."%(frute1,frute2))
#E2-7
num1=(input("첫 번째 숫자를 입력하세요:"))
num2=(input("두 번째 숫자를 입력하세요:"))


















