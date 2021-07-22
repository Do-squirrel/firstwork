def p_plus ( a, b) :
    print ( a + b )

def r_plus( a, b) :
    return  a + b 

p_result = p_plus(2,3)


# return은 값을 치환한다. fuction을 호출할 때, 즉 r_plus를 5로 바꿔야겠다.
# print 이런거 다 치우고 이제 return

def r_plus( a, b) :
    return  a + b 
    print ("sakfnklasdnfl", True)

r_result = r_plus(2,3)
print(r_result)

# return 밑의 함수는 절대 실행되지 않는다. return이 실행되자마자 함수가 끝
# 이제 print 말고 return을 쓰자.