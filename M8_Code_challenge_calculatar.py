# plus, minus, times, division, negation, power, reminder 계산기

def plus (a=0 , b=0) :
    return int(a) + int(b) 
    print("값을 제대로 입력해주세요")

print(plus( 7 , "10"))

def minus (a=0 , b=0) :
    return int(a) - int(b)
    print("값을 제대로 입력해주세요")

print(minus(0,"10"))

def times(a=0, b=0) :
    return int(a) * int(b)
    print("값을 제대로 입력해주세요")

print(times(10,"4"))

def division (a=0,b=1) :
    return int(a)/int(b)

print(division(7,"9"))
print(division(5))

def negation (a=0) :
    return -1*int(a)

print(negation("-7"))

def power (a=0,b=0) : # power는 제곱
    return int(a)**int(b)

print (power(10,"3"))

def reminder (a=0 , b=0) : # a를 b로 나눴을 때 나머지 연산자
    return int(a)%int(b)

print (reminder(7,3))

