# 정수형
a = 154
print(type(a))
a = 0
print(type(a))
a = -25
print(type(a))

# 양수 0 음수 모두 int 정수형인것 확인

# 실수형
b = 181.34
print(type(b))
b = -22.22
print(type(b))
# float 실수형으로 확인 가능 음수, 양수 소수점 다 실수형

# 복소수형
c = 1 + 4j
print(type(c))
print(c.real)
print(c.imag)
print(c.conjugate())
print(abs(c)) # 루트 형식으로 계산시 루트 17
# complex로 복소수의 타입도 확인 가능

# 예제 : 스스로 사칙연산을 활용해 확인

a = 5
b = 3.14 
c = 3 + 4j
print(10*a + 3*b + c)
# 수학적인 영역도 자동으로 알아서 계산해준다. c언어로하면 저세상임

