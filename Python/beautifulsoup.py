import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')
#old_content > table > tbody > tr:nth-child(2) > td.point
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    point = movie.select_one('td.point')
    if a_tag is not None:
        # a의 text를 찍어본다.
        print (a_tag.text, point.text)

ticket = soup.select('#reserveRanking0 > ul > li')

for movie in ticket:
    a_tag = movie.select_one('a')
    ratio = movie.select_one('span.ratio')
    if a_tag is not None:
        print(a_tag['title'], ratio.text)

