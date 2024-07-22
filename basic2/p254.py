#E7-1
def hello():
    print("안녕하세요")
for i in range(20):
    hello()
print()
#함수로 정의함
def uSum():
    sum=0
    for i in range(1,101):
        sum=sum+i
    print("합계: %d"%sum)
#만들어진 함수를 사용하는 쪽-비지니스 로직
uSum() #함수호출
uSum()

#하이픈만들기 함수로 정의
def hPrintr():
    print("-"*50)
hPrintr()

#합계가 3000이 넘는 순간 멈추고 합계, i값 출력하기
def bSum(n):
    sum=0
    for i in range(1,101):
        if sum>=n:
            break
        sum=sum+i
    print("%d이상일때 항목의 값 %d 합계 %d"%(n,i,sum))
bSum(3000)
uSum()
hPrintr()
#합계가 4000이 넘는 순간 멈추고 합계, i값 출력하기
bSum(4000)
uSum()
hPrintr()
#시작수와 끝수를 입력을 받아서 합계를 구해서 출력하기
sNum=int(input("시작수? "))
eNum=int(input("끝수? "))
uSum2=sNum+eNum
def uSum2():
    sum=0
    for i in range(sNum,eNum+1):
        sum=sum+i
    print(sum)
uSum2()







