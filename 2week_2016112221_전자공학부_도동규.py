# 문제 : 해달이는 1부터 100까지 숫자를 분류한다.
# 리스트 "mul2"에는 2의 배수, 리스트 "mul3"에는 3의 배수, 리스트 "mul6"에는 6의배수
# 나머지 수는 모두 더해서 출력, 해달이를 도와줘~

mul2=[]
mul3=[]
mul6=[]
others = 0
for i in range (1,101) :
    if (i%2==0) :
        mul2.append(i)
        mul2.sort
    elif (i%3==0) :
        mul3.append(i)
        mul3.sort

    if (i%6==0) :
        mul6.append(i)
        mul6.sort
    elif (i%2==0 or i%3==0) : None
    else : others+=i

print("mul2 =", mul2)
print("mul3 =", mul3)
print("mul6 =", mul6)
print("others =", others)


# 1633의 결과값이 나와야함