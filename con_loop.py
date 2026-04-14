import random

#1번
score = random.randint(1, 2000)
if score >= 1000:
    print("당신은 고수입니다.")
else:
    print("당신은 초보입니다.")

#2번
options = [0,100,200,300]
numA = random.choice(options)
numB = random.choice(options)
if numA == numB:
    print("두 값이 일치합니다.")

#3번
print("정수를 입력하세요 : ")
num = int(input())
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#4번
x = random.randint(-100, 100)
print("입력된 정수는 " + str(x) + "입니다.")
if x > 0:
    print("자연수입니다.")
elif x <= 0:
    print(x)

print("------------------------------")
print("next stage")

#1번
num = 2
if num > 0:
    print("True")

#2번
age = int(input("나이를 입력하세요 : "))
if age >= 10 and age < 19:
    print("청소년입니다.")

print("------------------------------")
print("next stage")

#1번
speed = random.randint(0, 150)
print("현재 속도는 " + str(speed) + "입니다.")
if speed >= 100:
    print("고속")
elif speed >= 60:
    print("중속")
else:
    print("저속")

print("------------------------------")
print("next stage")

#1번
firstQuestion = 0
for i in range(0, 101):
    firstQuestion += i
    
print(firstQuestion)

#2번
secondQuestion = 0
for i in range(0, 101):
    if i % 3 == 0:
        secondQuestion += i

print(secondQuestion)

#3번
Ala = [20,55,67,82,45,33,90,87,100,25]
thirdQuestion = 0

for i in Ala:
    if i >= 50:
        thirdQuestion += i

print(thirdQuestion)

#4번
fourthQuestion = 1
while True:
    print("*" * fourthQuestion)
    fourthQuestion += 1
    if fourthQuestion > 5:
        break   

print("------------------------------")
print("next stage")

#1번
quyatdrive = []
for i in range(1, 101):
        quyatdrive.append(i)

print(quyatdrive)

#2번
quyatdrive.clear()
for i in range(1, 101):
    if i % 2 == 0:
        quyatdrive.append(i)

print(quyatdrive)

#3번
quyatdrive.clear()
for i in range(1, 101):
    if i % 2 != 0:
        quyatdrive.append(i)

print(quyatdrive)

#4번
quyatdrive.clear()
for i in range(0, -101, -1):
    quyatdrive.append(i)

print(quyatdrive)   

print("------------------------------")
print("next stage")

#1번
for _ in range(0, 5):
    print("Hello, Python!")

#2번
for i in range(0, 5):
    print(i)


print("------------------------------")
print("next stage")


#1번
for i in range(1,101):
    print(i)

#2번
secondQuestion = 0
for i in range(0,1001):
    if i % 5 == 0:
        secondQuestion += i

print(secondQuestion)


#3번
thirdQuestion = 0
quyatdrive.clear()
quyatdrive = [70,60,55,75,95,90,80,85,100]

thirdQuestion = sum(quyatdrive) / len(quyatdrive)
print(round(thirdQuestion, 2))


#4번
quyatdrive.clear()
quyatdrive = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']

print(quyatdrive.count('A'))
print(quyatdrive.count('B'))
print(quyatdrive.count('AB'))
print(quyatdrive.count('O'))


#5번
numbers = [1,2,3,4,5]
result = [i * 2 for i in numbers if i % 2 == 1]
print(result)
