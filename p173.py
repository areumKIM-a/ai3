#C4-9
#1~200 출력 

'''for i in range(1,201,1):
    print(i,end=" ")
    if i==100:
        break


i=1
while i<=200:
    print(i, end=" ")
    if i==100:
        break   
    i=i+1'''

#100이면 빠지기
#100이면 찍지 않고 건너 뛰기(반복문은 계속) 101찍기

'''for i in range(1,201,1):
    if i==100:
        continue
    print(i,end=" ")
print()
print("-"*100)

i=1
while i<200:
    i=i+1
    if i==100:
        continue
    print(i,end=" ")'''

#C4-9 1부터 100까지 홀수의 누적합계

'''i=1
sum=0
cnt=0
while i<=100:
    if i%2==1:
        sum=sum+i
        print("%6d"%sum,end=" ")
        cnt=cnt+1

        if cnt%10==0:
            print()
    i=i+1'''

#C4-10
'''print("-"*30)
print("    달러   원화   유로")
print("-"*30)
dollar=10
while dollar<=100:
    won=dollar*1080
    euro=dollar*0.81
    print("%7d%8.0f%7.1f"%(dollar,won,euro))
    dollar=dollar+10
print("-"*30)

#C4-11
munjang=input("문장을 입력해 주세요: ")
i=len(munjang)-1
while i>=0:
    if munjang[i]==" ":
        print("-",end="")
    else:
        print("%s"%munjang[i],end="")
    i=i-1'''

#E4-1
'''for i in range(1,11,1):
    if i%2==1:
        print("%d"%i)
print("-"*30)
#E4-2
sum=0
for i in range(1,101,1):
    if i%3==0:
        sum=sum+i
print("1~100까지의 3의 배수 합계: %d"%sum)
#E4-3
for i in range(5,101,5):
    print(i,end=" ")'''
#E4-4
cnt=0
for i in range(1,101):
    if i%5==0:
        print(i,end=" ")
        cnt=cnt+1
        if cnt%5==0:
            print()

#E4-5
