#1번
def print_star():
    print("*" * 15)


print_star()

print("------------------------------")
print("next stage")

#1번
a = int(input("숫자 A를 입력하세요 : "))
b = int(input("숫자 B를 입력하세요 : "))
def print_sub(a, b):
    print(f"{a}과 {b}의 차는 {a - b}입니다.")

print_sub(a, b)

#2번
def print_mult(a , b):
    print(f"{a}과 {b}의 곱은 {a * b}입니다.")

print_mult(a, b)

print("------------------------------")
print("next stage")

#1번
def sum_nums(a):
    print(f"{len(a)}개의 인자 {a}")
    print(f"합계: {sum(a)}, 평균: {round(sum(a) / len(a), 1)}")


firstQuestion = (10,20,30)
sum_nums(firstQuestion)

firstQuestion = (10,20,30,40,50)
sum_nums(firstQuestion)
 

 #2번
def min_nums(a):
   print(f"최솟값은 {min(a)}")

secondQuestion = (20, 40, 50, 10)
min_nums(secondQuestion)


def report_card(name, *scores, bonus=0):
    total = sum(scores) + bonus
    avg = round(total / len(scores), 1)
    grade = ""
    if avg >= 90:
        grade =  "A"
    elif avg >= 80:
        grade =   "B"
    elif avg >= 70:
        grade =   "C"
    else:
        grade =   "F"
    print(f"학생: {name}")
    return (total, avg, grade)

total, avg, grade = report_card("홍길동", 85, 90, 78, bonus=5)
print(f"총점: {total}, 평균: {avg}, 등급: {grade}")
