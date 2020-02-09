import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

mise = rjson['RealtimeCityAir']['row']

for i in mise:
    if i['IDEX_MVL'] > 50:
        print (i['MSRSTE_NM'], i['IDEX_MVL'])