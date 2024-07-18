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
    print(i,end=" ")
#E4-4
cnt=0
for i in range(1,101):
    if i%5==0:
        print(i,end=" ")
        cnt=cnt+1
        if cnt%5==0:
            print()

#구구단
for i in range(1,10):
    for j in range(2,10):
        print("%3dx%2d=%3d"%(j,i,j*i),end=" ")
    print()

print("-"*100)

for i in range(2,10):
    for j in range(1,10):
        print("%3dx%2d=%3d"%(i,j,j*i),end=" ")
    print()'''
#소수 구하기
start=int(input("시작 수를 입력해주세요: "))
end=int(input("끝 수를 입력해주세요: "))
'''for x in range(start,end+1):
    for i in range(2,x):
        if x%i==0:
            break
        if x==i+1:
            print("%d"%x,end=" ")'''





