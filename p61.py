score=80
print("성적"+str(score))

x="토끼"*10
print(x)

n100="100"*20
print(n100)

n200=200
print(str(n200)*15)

x="수학성적:"
print(type(x))
y=80
print(type(y))
z=x+str(y)
print(type(z))

date="20220301"
year=date[0:4]
month=date[4:6]
day=date[6:]
date2=year+"-"+month+"-"+day
print(date2)
print(len(date))

#자기이름 5번(핸드폰번호마지막자리) 반복
name="김아름"
phone="010-2071-3595"
last_phone=phone[-1]
last_phone_int=int(last_phone)
print(last_phone_int)
print(name*last_phone_int)
print(int(phone[-1])*name)
phone="010-2071-3590"
end=phone[-1]
if end=="0" :
    print("10")
else :
    print("end")
print(name*int(end))

phone1="82-02-744-3334"
phone2="82-10-1234-4567"
'''
if len(phone2)==15 :
    print("한국 핸드폰번호입니다")
else :
    print("한국 집번호입니다")

if len(phone1)==15 :
    print("한국 핸드폰번호입니다")
else :
    print("한국 집번호입니다")
'''
if len(phone1)==15 and len(phone2)==15:
    print("phone1은 핸드폰번호입니다")
    print("phone2는 핸드폰번호입니다")
elif len(phone1)==15 and len(phone2)==14:
    print("phone1은 핸드폰번호입니다")
    print("phone2는 집번호입니다")
elif len(phone1)==14 and len(phone2)==15:
    print("phone1은 집번호입니다")
    print("phone2는 핸드폰번호입니다")
elif len(phone1)==14 and len(phone2)==14:
    print("phone1은 집번호입니다")
    print("phone2는 집번호입니다")

if phone1[3:5]=="10" and phone2[3:5]=="10":
    print("phone1은 핸드폰번호입니다")
    print("phone2는 핸드폰번호입니다")  
elif  phone1[3:5]=="10" and phone2[3:5]=="02":
    print("phone1은 핸드폰번호입니다")
    print("phone2는 집번호입니다")
elif phone1[3:5]=="02" and phone2[3:5]=="10":
    print("phone1은 집번호입니다")
    print("phone2는 핸드폰번호입니다")
elif phone1[3:5]=="02" and phone2[3:5]=="02":
    print("phone1은 집번호입니다")
    print("phone2는 집번호입니다")










