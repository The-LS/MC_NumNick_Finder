import requests
from bs4 import BeautifulSoup
import time
ser = int(input("시작 숫자를 입력하세요:"))  # 시작 숫자
se = ser
res = int(input("마지막 숫자를 입력하세요:"))  # 마지막 숫자
add = 0  # 진행 상황(1)
qkf = 0  # 찾은수
minus = 10
wnr = 0  # 주기 변수
awd = 0
w = res-ser
wn = round(w/10) #주기
wf = round(w/100)
fon = []  # 찾은 문자
fa = 0 #시도횟수
at = time.strftime('%Y-%m-%d', time.localtime((time.time())))
start_time=time.time()
f = open(f"./Nick-log.txt", "a")
while ser < res + 1:
    fa = fa + 1
    ser = ser + 1
    wnr = wnr + 1

    if wnr == wn:
        wnr = 0
        add = add + 1
        minus = minus - 1

    url = 'https://mcname.info/ko/search?q='
    response = requests.get(url + str(ser))
    if fa == wf:
        awd = awd + 1
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#status-bar > div > div.col-lg-8.text-center > p')
        check = soup.find("div", attrs={"class":"col-sm-6 my-1"}).get_text()
        if check == """
상태
유효한
""":
            qkf = qkf + 1
            fon.append(ser)


    else:
        print(response.status_code)

    en = "🟥" * add
    ne = "🟩" * minus
    if len(fon) > 3:
        sea = f"[{fon[0]}, {fon[1]}, {fon[2]}.......]"

        going = f"""






















                [마인크래프트 숫자 닉네임 검색기]
                범위: {se} ~ {res}    검색중인 닉네임 : {ser}    현재 검색 상태:정상
                현재 검색 진행 상황...       
                {fa}/{w}[{en}{ne}]       
                검색된 사용 가능한 닉네임    {len(fon)}/{fa}
                {sea}              자세한 정보는 ./Nick-log.txt 에 기록됨
                검색중인 URL: {url + str(ser)}         
                """
        print(going)
    else:
        going = f"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        [마인크래프트 숫자 닉네임 검색기]
        범위: {se} ~ {res}    검색중인 닉네임 : {ser}    현재 검색 상태:정상
        현재 검색 진행 상황...       
        {fa}/{w}[{en}{ne}]       
        검색된 사용 가능한 닉네임    {len(fon)}/{fa}
        {fon}                      
        검색중인 URL: {url + str(ser)}         
        """
        print(going)

end_time=time.time()
total_time=str(end_time-start_time)
if ser == res + 1:
    if len(fon) > 3:
        sea = f"[{fon[0]}, {fon[1]}, {fon[2]}.......]"
        print(f"""
    
    
    
    
    
    
    
    
    
    
        [마인크래프트 숫자 닉네임 검색기]
        범위: {se} ~ {res}    검색중인 닉네임 : None
        현재 검색 진행 상황...         현재 검색 상태...
        [None]                         [검색 완료]
        검색된 사용 가능한 닉네임
        {sea}
        검색중인 URL: None
        찾은수 : {len(fon)}      걸린시간 : {total_time[:3]}s
        """)
    else:
        print(f"""











                [마인크래프트 숫자 닉네임 검색기]
                범위: {se} ~ {res}    검색중인 닉네임 : None
                현재 검색 진행 상황...         현재 검색 상태...
                [None]                         [검색 완료]
                검색된 사용 가능한 닉네임
                {fon}
                검색중인 URL: None
                찾은수 : {len(fon)}      걸린시간 : {total_time[:3]}s
                """)

f.write(f"""
[Mc Nick Searcher]-{at}
Length: {se} ~ {res}
Searched useable nick    {len(fon)}/{fa}
{fon}                  
Used  Time : {total_time[:4]}s
Found : {len(fon)}

""")
f.close