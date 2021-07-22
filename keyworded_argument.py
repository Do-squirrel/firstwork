# 지금까지 사용한 인자는 Positional argument, 위치에 영향을 받는 인자.
# keyword argument는 위치에 따라 정해지는게 아닌 이름으로 쌍을 지어준다.
# 즉 위치에 상관없이 내가 인자만 기억하고 있으면 적어주면 된다.


def say_hello( name, age):
    return f"Hi {name} you are {age} old"

hello = say_hello (name="nico", age="12")
print (hello)

# 되는데 왜 오류라고 뜨지...
# string안에 변수를 포함하고 싶으면 맨처음에 f(format)을 표시하고 {}로
# 변수들을 감싸면된다.
