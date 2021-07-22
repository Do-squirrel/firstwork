# 시험 점수에 따른 과락 분류

score = int(input('점수를 입력하세요'))

if score >= 70 :
     result = "통과"
elif score >= 60 : 
    result = "재시험"
elif score >= 50 :
    result = " 평균"
else : 
    result = "과락"

print (result)

# if 문의 구조
# if 조건문 :
    # 실행할 코드 1
    # 실행할 코드 2
# if 문 코드 탈출하고 실행할 코드 1