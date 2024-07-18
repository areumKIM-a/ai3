'''for i in range(2):
    phone=input("하이픈을 포함한 휴대폰번호를 입력하세요: ")
    for x in phone:
        if x!="-":
            print("%s"%x,end="")
    print()'''

'''phone=input("휴대폰번호를 입력하세요: ")
for i in phone:
    if 'A'<=i<='Z' :
        print("%s"%i,end="")'''
#대문자, 소문자 빼고 출력
#phone=input("휴대폰번호를 입력하세요: ")
'''for i in phone:
    if not('A'<=i<='Z' or'a'<=i<='z' or'0'<=i<='9'):
        print("%s"%i,end="")'''
'''for i in phone:
    if '가'<=i<='힣':
        print("%s"%i,end="")'''

'''print("-"*30)
print(" 섭씨 화씨")
print("-"*30)
for i in range(-20,31,5):
    f= i*9.0/5.0+32.0
    print("%5d %6.1f"%(i,f))
print("-"*30)'''

#C4-1
'''cnt=0
for i in range(200,801):
    if i%5!=0:
        print("%d"%i,end=" ")
        cnt=cnt+1

        if cnt%10==0:
            print()'''

'''num=input("숫자를 입력하세요: ")
cnt=0
for a in num:
    a=int(a)
    if a%2==1:
        cnt=cnt+1
print("홀수의 개수: %d개"%cnt)'''

#C4-7
#깃이 관리하나?
print("aaa")

