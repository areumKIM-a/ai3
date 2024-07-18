'''word="I am happy"
for i in word:
    print(i,end="")
print()
print(word)'''

'''phone="010-3744-3334"
print(phone)
#핸드폰번호안에 5가 있나요? 답 없습니다
flag=0
for i in phone:
    if i=="5":
        flag=1
       
if flag==0:
    print("없어요")
else:
    print("있어요")'''

#영어문장에 "a"가 있나요?
#word="apple"
#word="an/a"
#word="book"
for j in range(0,3,1):
    word=input("영어 단어는?")
    flag=0
    cnt=0
    for i in word:
        if i=="a":
            flag=1
            cnt=cnt+1
    if flag==0:
        print("a가 없어요")
    else:
        print("%d개 있어요"%cnt)
