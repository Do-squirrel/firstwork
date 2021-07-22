# for문은 정해진 만큼만 돌리는 상황, while은 정해진 목표까지 돌린다

# while문 기초
it = 0
while it < 5 :
    it += 1
    print (it)
# 맨 처음 it을 0으로 주고 while로 it이 5보다 작을 때 계속 돌아간다.
# it에 1씩 더하는데 5보다 작으면 계속 print 하라

# while 문의 구조, 앞에서 뭔가 지정은 해줘야 할듯?
# while 조건 :
    # 반복할 명령어 1
    # 반복할 명령어 2

# while 무한 루프 + break
it = 0 
while True :
    it +=1 
    print (it)
    if it >= 500 :
        break


