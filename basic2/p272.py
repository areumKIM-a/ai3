#E7-10
'''def func(c):
    x=c+5
    return x

r=func(100)
print(r)#105

#함수정의
def inchToCm(inch):
    cm=[]
    for i in range(10,31,10):
        k=i*2.54
        cm.append(k)
    return cm
#함수호출
result=inchToCm(10)
print(result)'''

'''cm=inch*2.54
    #*10,*20,*30
    return cm'''
#함수호출;
'''s=inchToCm(100)
print(s)'''
#120
def p(n):
    result=[]
    answer=1
    for  i in range(n,0,-1):
        answer=answer*i
    result.append(answer)
    answer=0
    for  i in range(1,n+1):
        answer=answer+i
    result.append(answer)
    answer=0
    for  i in range(1,n+1):
        answer=answer*+1
    result.append(answer)
    return result
print(p(5))

#결과 5!결과==>120, 1~5까지 합==>15, 1~5까지 길이==>5








