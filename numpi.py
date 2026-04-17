import numpy as np

#1번
arr1 = np.arange(15,24)
matrix1 = arr1.reshape(3,3)
print(matrix1)

#2번
arr2 = np.arange(1,9)
matrix2 = arr2.reshape(2,4)
print(matrix2)

result = (matrix2[0] == matrix2[1])
print(result)

#3번
first = np.array([15,100,45])
second = np.array([78,25,90])
mission = np.array([81,45,99])

total = 0.4 * first + 0.4 * second + 0.2 * mission + 5
print("각 학생 최종점수: ",total)
print("중간고사 평균: ", first.mean())
print("중간고사 표준편차: ", first.std())
print("철수 최종점수: ", total[0])

print("-" * 30)
print("next stage")

#1번
arr1 = np.arange(15,24)
matrix1 = arr1.reshape(3,3)
print(matrix1)

#2번

