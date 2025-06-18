from django.shortcuts import render
import requests
import json

### 전역변수
dlist = []  # list함수에서 공공데이터를 가지고 와서 view함수에 전달

# 공공데이터 리스트
def list(request):
    global dlist #전역변수 사용
    # 공공데이터 가져오기에 필요한 정보
    pageNo = 1
    serviceKey = '918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    url = f'https://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={serviceKey}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    
    # 공공데이터 가져오기
    response = requests.get(url)          # 공공데이터 가져온 타입 : str타입
    json_data = json.load(response.text)  # json타입으로 변경 -> dict타입
    
    a = {'id':'aaa','pw':1111}
    print(a['id'])
    
    return render(request,'pboard2/list.html')
