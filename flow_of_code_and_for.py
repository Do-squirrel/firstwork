# 프로그램 코드의 흐름 순차, 반복, 조건
# if elif else 구문
# 순차구조 줄넘버 1번부터 n번까지 순차대로 진행
a = 154
print(type(a))
a = 0
print(type(a))
a = -25
print(type(a))

# for문 무작정 따라하기
for i in range (1,11) :
    if (i%2 == 0) :
        print (i, "은/는 짝수 입니다.")
    else     :
        print (i, "은/는 홀수 입니다.") 

# for문의 구조
# for i in 범위 :
    # 반복할 명령어 1
    # 반복할 명령어 2
    # ctrl + / 하면 바로 주석처리 

mylist = ["해달이", '사스미', "메기"]
for i in mylist :
    print ((i))


print ("반복 끝")

# print list with range
print (list(range(1,11))) # 시작점을 주고 시작
print (list(range(10))) # 시작점을 안주면 0부터 시작
print (list(range(1,20,3))) # 3칸씩하면서 진행
print (list(range(20,1,-3))) # -3칸씩 진행

# for문 with range
for i in range(1,11) :
    print (i, end=" ") # i가 끝날 때 마다 end = " " 스페이스바로 띄운것
print ("반복 끝")