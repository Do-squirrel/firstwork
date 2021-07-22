# 리스트
# 리스트_이름 = [요소1, 요소2, 요소3...]
# 리스트가 하나의 큰 박스라고 생각하면 쉽다

# 리스트 선언

Haedal_character = ["해달이", "시라용", "아리", "메기", "사스미"]

# 빈 리스트 
mylist = []
print (mylist)

# 파이썬 리스트 특징 - 요소들의 자료형을 통일하지 않아도 된다.
# 그냥 적은대로 리스트에 있는걸 다 보여준다
mylist = [1, 2, "해달이", True, ['a', 'b', 'c']]
print (mylist)

# 리스트 인덱싱 Indexing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# 인덱싱의 가장 중요한 점은 컴퓨터는 첫 번째를 0번째라고 시작한다.
print (a[0]) # 1
print (a[5]) # 6
print (a[9]) # 10
#print (a[10]) # range error

# 음수 인덱싱, 위의 a 리스트에서 끝에서 부터 -1 즉 10이 -1 9는 -2..
print (a[-1]) #10
print (a[-5]) # 6

# 리스트 슬라이싱 시작 끝부분 정해놓고 하는것
print (a[0:3]) # 1,2,3
print (a[1:3]) # 2,3 
print (a[:3]) # 처음부터 3번째 까지
print (a[7:]) # 8 9 10
print (a[:]) # 전체 가져오기
print (a[-4:-2]) # 슬라이싱 숫자가 몇번쨰꺼 가져오는지는 잘보기

# 리스트 수정 
a[0] = 100 # a의 0자리에 100을 넣고싶다. 즉 첫번째에 100
print (a) 

# 리스트 삭제
del a[0] # 리스트 a의 첫번째 삭제
print (a)
del a[3:]
print (a) # 리스트 a의 3이후 전부 삭제

# 리스트의 길이 확인, 정렬, 값을 추가 등.. "리스트 내장 함수"
# 리스트 길이 구하는 len()
a = [1,2,3,4]
print(len(a)) # 4

# 리스트의 값을 추가해주는 append()
mylist = [ 'a', 'b', 'c', 'd']
mylist.append('e')
print (mylist) # append 는 리스트 마지막에 추가된다

# 리스트의 값을 정렬해주는 sort()
mylist = [4,2,3,1]
mylist.sort() # 숫자를 아무거나 리스트 해놧는데 sort로 정렬
print (mylist) # 1, 2, 3, 4
mylist.sort(reverse=True) 
print (mylist) # 4, 3, 2, 1