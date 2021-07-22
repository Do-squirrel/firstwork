# 기본 문자열, 문자열을 만드는 방법

s2 = 'Hello, Haedal!'
print (s2)

S2 = "Hello, Haedal!"
print (S2)

s6 = '''Hello, Haedal!''' 
print (s6)

S6 = """Hello, Haedal!"""
print (S6) # 트리플 쉼표도 가능

# 이스케이프 코드
# \n, \t, \\,\',\"

longtext1 = """Hello, Haedal!
my name is Haedal programming""" # 트리플 쉼표는 엔터하면 그냥 바로 줄바꿈이 된다
print (longtext1)

longtext2 = 'Hello, Haedal!\nmy name is Haedal programming'
print (longtext2)
#이스케이프 코드 \n을 사용하면 엔터 처리가 되어서 나온다.

# String Interpolation
a = 123 
new_q = f'{a}'
print(new_q)
# 인터폴레이션? 알아두면 편하다는데  잘..

# 문자열 옛날 방식
print(f'%s %s' % ('one', 'two'))
# 퍼센트로 표시한 부분 자리에 맞게 적어줘야해서 불편

# pyformat 
print('{} {}'. format('one', 'two'))

# f-string
a, b = 'one' , 'two'
print (f'{a} {b}')
print (f'{b} {a}')

# example 
name = "해달"
eng_name = "Haedal"
print("안녕하세요, {1}입니다. My name is {0}". format(eng_name, name))
print(f'안녕하세요 {name}입니다.')


# 문자열 인덱싱
a ="Hello, Haedal!"
print (a[1]) #e

# 문자열 슬라이싱
a = "Hello, Haedal!"
print (a[4:9])

# 문자열 길이를 구하는 len()
print(len(a))

# 문자열의 최대, 최소를 구하는 max(), min()
# 문자열을 알파벳과 숫자에서 가장 큰 값을 알아낸다
# 아스키코드 -> 
a = "312"
b = 'bac'
print (min(a))
print (max(b))
print (max(a))
print (min(b))

print (min(a+b)) # 1 
print (max(a+b)) # c
# 아스키 코드떄문에 숫자가 앞이고 문자열이 뒤라서 나온 결과

# 소문자, 대문자로 변환해주는 lower() , upper()

a = 'This is apple'
print(a.upper()) # 싹다 대문자
print(a.lower()) # 싹다 소문자

# 문자열을 구분자에 따라 나누는 split()
a = ' 안녕, 나는, 해달이야.'
print (a.split(sep=',')) # split 해서 ,마다 잘라서 리스트의 요소로 넣은것

b = "안녕 나는 해달이야"
print (b.split()) # 그냥 빈칸으로 넣으면 띄어쓰기를 구분해서 스플릿

# 여러개의 문자열 사이에 구분자를 넣어주는 join()
mylist = ['안녕', '나는', '해달']
mystring = '_'. join(mylist)
print (mystring) #안녕_나는_해달
