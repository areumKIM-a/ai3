#E7-7
#매개변수를 가변적으로 하고 싶을때 *args
#비지니스로직  부분(실제 코드 수행 부분) 함수 호출
def average(*args):
    print(args)
    print(len(args))
average(85,96,87)
average(77,93,85,97,72)

def func(food):
    for x in food:
        print(x)
fruits=["사과","오렌지","바나나"]
func(fruits)

#E7-9
def func(food):
    food.append("딸기")
    food.append("수박")
fruits=["사과","오렌지","바나나"]
print(fruits)
func(fruits)
print(fruits)
#C7-1
def add(a,b):
    c=a+b
    print("%d+%d=%d"%(a,b,c))
add(12,15)
add(245,300)
add(-38,-12)
#C7-2
def sum_int(start,end):
    total=0
    for i in range(start,end+1):
        total=total+i
    print("%d~%d 정수 합계: %d"%(start,end,total))
sum_int(20,50)
sum_int(600,800)
#C7-3
def member_join(*args):
    result=""
    for i in args:
        result=result+i+" "
    print("가입회원: %s"%result)
member_join("김정연","안서영")
member_join("황선형","김철영","이창연")
member_join("정수진","김보람","정수연","함소영")
#C7-4
def multiply(num,x):
    i=0
    while i<len(num):
        num[i]=num[i]*x
        i=i+1
numbers=[10,20,30,40,50]

multiply(numbers,10)
print(numbers)
multiply(numbers,10)
print(numbers)
