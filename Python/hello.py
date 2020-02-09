print("hello")

def sum_all(a,b,c):
    return a+b+c

def mul(a,b):
    return a*b

result = sum_all(1,2,3) + mul(10,10)

def minus(a,b):
    return a-b

result2 = minus(mul(10,10),sum_all(1,2,3))

print(result2)

a = 1
b = 2

if a < b :
    print(a)

print('----------------------------------')

age = 10

if age < 20:
    print("성인이 아닙니다.")
else:
    print("성인 입니다.")

for i in range(0, 10):
    print(i)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7}
]

for person in people:
    print(person['name'], person['age'])

print('----------------------------------')

a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

for fruit in a:
    print(fruit + "입니다.")

a = 'spartacodingclub@gmail.com'
b = 'djkdjkd'
c = 'a@a.com'

def check_mail(s):
    if s.find('@') == -1:
        return False
    else:
        return True
#결과값
print(check_mail(a))
print(check_mail(b))
print(check_mail(c))
print(check_mail('email'))

a = 'spartacodingclub@gmail.com'
b = 'dnkdj@naver.com'
c = 'djifeij@daum.net'

#채워야하는 함수
def get_mail(s):
    return s.split('@')[1].split('.')[0]
#결과값
print(get_mail(a))
print(get_mail(b))
print(get_mail(c))

#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
  result = {}
  for element in a_list:
    if element in result:
      result[element] += 1
    else:
      result[element] = 1
  return result

#결과값
print(count_list(a))

import random

def get_lotto():

    lotto = []
    for i in range(6):
        num = random.randrange(1, 47)
        lotto.append(num)
    return 

    print(get_lotto())

#아래와 같이 출력됩니다
[4, 46, 19, 34, 39, 43]





