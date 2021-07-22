# list와는 다르게 common operation만 가능
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

print(type(days)) # class 'tuple'로 나온다.
# tuple은 고정된거라서 바꿀 수가 없다. 아무도 변경할 수 없는 리스트라고 생각하자
# 괄호로 하는 것 , 길이 max min 등을 얻을 수 있다.


#dictionary를 만들어보자
name = "nico"
age = 27
korean = True
fav_food = ["kimchi", "sashimi"]
# 여기까지는 다 변수가 된다 dictionary는 nico에 대한 정보를 싹다 넣는것

nico = {
    "name" : "nico",
"age" : 27,
"korean" : True,
"fav_food" : ["kimchi", "sashimi"]
}
print(nico)

nico["handsome"] = True
# dictionary로 nico에 대한 정보를 만든것. 변수마다 ""를 넣어주고 : 로 value를 넣어준다.
# dictionary 뒤에 원하는 정보를 추가 할수 있다.