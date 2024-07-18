# sum=0
# for i in range(1,11) :
#     print(i)
#형식 range(초기값,최종값-1,증가값) 초기값(기본은 0)과 증가값(기본은 1)은 생략가능
# sum=0
# for i in range(0,11,2) :
#     sum=sum+i
#     print("i의 값 : %d=> 합계: %d"%(i,sum))

#p146 E4-4
# sum=0
# for i in range(10):
#     print(i,end=" ")
# print()
# for i in range(1,11):
#     print(i,end=" ")
# print()
# for i in range(1,10,2):
#     print(i,end=" ")
# print()
# for i in range(20,0,-2):
#     print(i,end=" ")
# print()

#p149 E4-5
sum=0
cnt=0
for i in range(5,101,5):
    print(i,end=" ")
    cnt=cnt+1
print()
print("갯수는= %d개"%cnt)
cnt=0
for i in range(4,201,4):
    print(i,end=" ")
    cnt=cnt+1
print()
print("갯수는= %d개"%cnt)
cnt=0
for i in range(200,-201,-50):
    print(i,end=" ")
    cnt=cnt+1
print()
print("갯수는= %d개"%cnt)
