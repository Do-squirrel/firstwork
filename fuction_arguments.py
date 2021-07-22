#def say_hello(who) :
    #print ("hello" , who)

# ()안에 input을 넣어야한다. def에서는 fuction의 이름을 정의했다.
# say_hello() 괄호안에 인자를 넣을수 있다. 즉 fuction을 실행할떄 who where 등..

#say_hello("Nicolas")
# who 가 니콜라스가 되고 print 뒤에도 , 로 순서를 정해준다.
# 즉 fuction에 데이터를 주는 개념

# 계산기의 덧셈과 뺄셈..
def plus (a, b=0) :
    print ( a + b ) 

def minus (a,b=0) :
    print (a - b)

plus( 2, 5)

minus ( 2, 5 )

# plus, minus 라는 fuction을 만들어 준것.
# default value 라는 것을 넣어서 a 만 넣었을때도 값이 나올수있게 b=0을 대입하면 자동으로 b가 안들어간것으로 처리된다.
