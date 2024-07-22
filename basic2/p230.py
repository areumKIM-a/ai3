animals=('토끼','거북이','사자','여우') #소괄호는 튜플임
print(animals)

numbers=tuple(range(10))
print(numbers)

print(animals[1])
print(numbers[3])

#수정하기
#animals[2]='호랑이'됨

anNum=animals+numbers
print(anNum)

#for문
n2=tuple(range(101))
s=0
for i in n2:
    s=s+i
print(s)
print(sum(n2))


