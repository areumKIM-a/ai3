#딕셔너리
'''member={'name':'황예린','age':22,'email':'yerin@hanmail.net','age':30} #{키:값}
print(member['name'])
print(member['age']) #두번 넣으면 마지막 값이 출력됨
print(member['email'])

score=dict([('국어',80),('영어',90),('수학',100)])
print(score)
print(score['국어'])
print(score,'~~~')
#국어점수 90점으로 수정하기
score['국어']=90
score2=dict([['국어',80],['영어',90],['수학',100]])
print(score2)
print(score2['수학'])
#국어점수 90점으로 수정하기
score2['국어']=90
print(score2,'@@@')'''
#C6-1
print("구구단표")
print("="*60)
dans=(2,3,4,5,6,7,8,9)
for i in dans:
    print("%d단"%i)
    for j in range(1,10):
        print("%dx%d=%d"%(i,j,i*j))
    print("-"*60)
#E6-8
user={"id":"kim55","name":"강성준","level":7,"point":10000}
print(user)
print(user["id"])
print(user["name"])
print(user["point"])
#E6-9
scores={"kor":90,"eng":89,"math":98}
print(scores)
scores['music']=100
print(scores)
#6-10
words={'door':'문','chair':'의자','table':'책상','house':'집'}
print(words)
words['table']="테이블"
print(words)
words["house"]="하우스"
print(words)
print()
#E6-11
car={"brand":"현대","model":"아반테","start":"1990","year":2021}
print(car)
i=car.pop("start")
print(i)
print(car)
print()
#E6-12
car={"brand":"현대","model":"아반테","start":"1990","year":2021}
print(car)
car.clear()
print(car)
print()
#E6-13
areaCode={"서울":"02","부산":"051","대구":"053","광주":"062"}
for key in areaCode:
    print("%s 지역번호: %s"%(key,areaCode[key]))
print()
#C6-2
scores={"김채린":85,"박수정":98,"함소희":94,"안예린":90,"연수진":93}
sum=0
for key in scores:
    print("%s : %d"%(key,scores[key]))
    sum=sum+scores[key]
avg=sum/len(scores)
print("합계 : %d, 평균 : %.2f"%(sum,avg))
print()
#C6-3
admin_info={"id":"admin","password":"12345"}
input_id=input("아이디를 입력하세요: ")
input_pass=input("비밀번호를 입력하세요: ")
if input_id==admin_info["id"] and input_pass==admin_info["password"]:
    print("정보에 접근 권한이 있습니다")
else:
    print("정보에 접근 권한이 없습니다")
print()
#C6-4
words={"꽃":"flower","나비":"butterfly","학교":"school","자동차":"car","비행기":"airplane"}
print("<영어 단어 맞추기 퀴즈>")
for key in words:
    input_word=input("%s에 해당되는 영어 단어를 입력해주세요: "%key)
    if input_word==words[key]:
        print("정답입니다!")
    else:
        print("틀렸습니다!")
print()







