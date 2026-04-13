# 1번
even_list = [2, 4, 6, 8, 10]
print(even_list)

# 2번
ever_list = []
for i in range(1, 11):
    if i % 2 == 0:
        ever_list.append(i)

print(ever_list)

# 3번
nations = ["Korea", "Japan", "China", "USA", "UK"]
print(nations)

# 4번
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(friends)

#5번
string = ["X","Y","Z"]
print(string)

#-------------------------------------------
print("------------------------------")
#1번
n_list = []
for i in range(0, 15):
    n_list.append(i)

#2번
s_list1 = n_list[0:5]
print(s_list1)
s_list2 = n_list[5:10]
print(s_list2)
s_list3 = n_list[11:15]
print(s_list3)
s_list4 = n_list[2:11:2]
print(s_list4)
s_list5 = n_list[10:5:-1]
print(s_list5)
s_list6 = n_list[10:0:-2]
print(s_list6)

#-------------------------------------------
print("------------------------------")

#1번
a = [1,2,3]
b = [10,20,30]
a.append(b)
print(a)
#[1,2,3,[10,20,30]]

#if not use append, but use extend
#[1,2,3,10,20,30]

#2번
nlist = [1,2,3,4,5,6,7,8,9,10]
print(nlist)

#3번
nlist.insert(0, 0)
print(nlist)

#4번
nlist.reverse()
print(nlist)

#5번
alpha = nlist.pop(-1)
print(alpha)
print(nlist)

#-------------------------------------------
print("------------------------------")

#1번



