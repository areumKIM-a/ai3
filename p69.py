'''name=input("이름은")
print(name)'''

'''age=input("당신의 나이는?")
print("당신의 나이는 %s살입니다"%age)
print("당신의 나이는 %d살입니다"%int(age))'''

#입력: 출생연도 출력: 당신은 ?살입니다
'''birthYear=input("출생연도")
print("당신은 %d살입니다"%(2024-int(birthYear)))'''

'''address=input("사는곳 ")
print("당신이 사는 곳은 %s입니다"%address)'''

'''birth=input("출생년월")
manAge=202407-int(birth)

print("당신의 만나이는 %d살입니다"%(manAge[0:3]'''

'''a=input("첫 번째 정수를 입력하세요")
b=input("두 번째 정수를 입력하세요")
c=a+b
print(c)'''

'''a=input("첫 번째 정수를 입력하세요")
b=input("두 번째 정수를 입력하세요")
c=int(a)+int(b)
print(c)'''

#중간값 구하기
'''a=input("첫 번째 정수를 입력하세요")
b=input("두 번째 정수를 입력하세요")
c=input("세 번째 정수를 입력하세요")
if int(a)!=max and int(a)!=min :
    print(a)
elif int(b)!=max and int(b)!=min :
    print(b)
elif int(c)!=max and int(c)!=min :
    print(c)'''

#큰값 구하기
'''a=input("첫 번째 정수를 입력하세요")
b=input("두 번째 정수를 입력하세요")
c=input("세 번째 정수를 입력하세요")
if int(a) > int(b) and int(a) > int(c):
    print(a)
elif int(b) > int(a) and int(b) > int(c):
    print(b)
elif int(c) > int(a) and int(c) > int(b):
    print(c)'''

'''a=int(input("첫 번째 정수를 입력하세요"))
b=int(input("두 번째 정수를 입력하세요"))
c=int(input("세 번째 정수를 입력하세요"))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)'''

a=int(input("첫 번째 정수를 입력하세요"))
b=int(input("두 번째 정수를 입력하세요"))
c=int(input("세 번째 정수를 입력하세요"))
print(max(a,b,c))


     








