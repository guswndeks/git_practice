import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

url = "https://books.toscrape.com/"
res = requests.get(url)

if res.status_code != 200:
    print("접속불가, 자동 종료")
    exit()
print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')
books = []
count = len(soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'))
for i in range(0,count):
    data = soup.find_all(class_='product_pod')[i]
    title = data.h3.text
    rate = data.find('p')['class'][1]
    books.append([title, rate])

for i in range(0,count):
    print(f"제목 : {books[i][0]}, 평점 : {books[i][1]}")


# --- 웹 화면 ---
st.title('책 가격 비교')
keyword = st.text_input('책 제목 검색')

df = pd.DataFrame(books, columns=['title', 'rate'])
if keyword:
    df = df[df['title'].str.contains(keyword, case=False)]

st.dataframe(df)