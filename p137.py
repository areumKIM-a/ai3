# su=input("수를 입력하세요: ")
# jarisu=len(su)
# su=int(su)
# if jarisu==1:
#     print("%s는 한 자리 숫자이다"%su)
# elif jarisu==2:
#     print("%s는 두 자리 숫자이다"%su)
# elif jarisu==3:
#     print("%s는 세 자리 숫자이다"%su)
# elif not (0<=su<=999):
#     print("오류! %s은 범위(0~999) 이외의 숫자이다"%su)

#E3-8
# num1=int(input("첫 번째 숫자를 입력하세요: "))
# num2=int(input("두 번째 숫자를 입력하세요: "))
# print("원하는 연산은")
# yunsan=input("+,-,*,/ 중 하나를 선택하세요:")
# if not(yunsan=="+" or yunsan=="-" or yunsan=="*" or yunsan=="/"):
#     print("선택 오류!")
# elif yunsan=="+":
#     print("%d+%d=%d"%(num1,num2,num1+num2))
# elif yunsan=="-":
#     print("%d-%d=%d"%(num1,num2,num1-num2))
# elif yunsan=="*":
#     print("%d*%d=%d"%(num1,num2,num1*num2))
# elif yunsan=="/":
#     print("%d/%d=%.2f"%(num1,num2,num1/num2))

#S3-2
# hour1=int(input("첫 번째 시간의 시를 입력하세요: "))
# minute1=int(input("첫 번째 시간의 분를 입력하세요: "))
# hour2=int(input("두 번째 시간의 시를 입력하세요: "))
# minute2=int(input("두 번째 시간의 분를 입력하세요: "))
# if not(0<=hour1<=24 and 0<=hour2<=24 and 0<=minute1<=59 and 0<=minute2<=59):
#     print("시간과 분을 잘못 입력하셨어요")
# elif hour1<hour2 :
#     print("빠른 시간: %d:%d"%(hour1:minute1))
#     print("느린 시간: %d:%d"%(hour2:minute2))
# elif hour1==hour2 and minute1<minute2:
#     print("빠른 시간: %d:%d"%(hour1:minute1))
#     print("느린 시간: %d:%d"%(hour2:minute2))
# elif hour1<hour2 and minute1>minute2:
#     print("빠른 시간: %d:%d"%(hour1:minute1))
#     print("느린 시간: %d:%d"%(hour2:minute2))
# else :
#     print("빠른 시간: %d:%d"%(hour2:minute2))
#     print("느린 시간: %d:%d"%(hour1:minute1))

