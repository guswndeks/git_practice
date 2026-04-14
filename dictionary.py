#1번
dic = {"name": "홍길동", "birth": 1128, "age": 30}
print(dic)

#2번
# 정답은 3번, 해당 타입은 리스트에 해당

#3번
a = {'A':90, 'B':80, 'C':70}
print(a['B'])
del a['B']
print(a)

#4번
a.clear()
a = {'A':90, 'B':80}
a['C'] = 70
print(a)

#5번
print(min(a.values()))

#6번
a_list = list(a.items())
print(a_list)

print("------------------------------")
#1번
fruits_dic = {"apple": 6000, "banana": 5000, "melon": 3000, "orange": 4000}
print(list(fruits_dic.keys()))

#2번
print(list(fruits_dic.values()))

#3번
print(len(fruits_dic.keys()))

#4번
if "apple" in fruits_dic:
    print("apple is in fruits_dic.")
else:    
    print("apple is not in fruits_dic.")
if "mango" in fruits_dic:
    print("mango is in fruits_dic.")
else:    
    print("mango is not in fruits_dic.")

