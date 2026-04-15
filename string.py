code = "881120-1068234"
birth = "20" + code[0:6]
sex = code[7]
a = "a:b:c:d"
a = a.replace(":", "#")
print(birth)
print(sex)
print(a)

url = "http://naver.com"
url = url.replace("http://", "")
print(url)
point = url.find(".")
url = url.replace(url[point:], "")
print(url)
line1 = url[0:3]
line2 = len(url)
line3 = url.count("e")
print(line1 + str(line2) + str(line3))