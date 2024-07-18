'''#키보드로 이름을 입력 받아보세요
name=input("이름은?")
#이름을 화면 출력하기
print("입력한 이름은 %s입니다"%name)
#키보드로 포인트점수를 입력 받아 보세요
point=input("포인트점수는?")
#포인트 점수의 20%는 600점 입니다
pointValue=int(point)
point20Per=pointValue*0.2
print("포인트 점수의 20%","는 %d점입니다"%point20Per,sep="")'''

#당신의 주소는? 강동구
address=input("당신의 주소는?")
#몇번 반복 할래요?
'''banbok=input("몇번 반복 할래요?")
print(address*int(banbok))'''
#출력 당신의 주소글자는 힌트len()
print(len(address))
