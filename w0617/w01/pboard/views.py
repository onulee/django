from django.shortcuts import render
import requests
import json

list = []

# 공공데이터 상세보기
def view(request,galContentId):
    print('넘어온 galContentId : ',galContentId)
    print('공공데이터 리스트 : ',list)
    return render(request,'pboard/view.html')


# 공공데이터 리스트
def list(request):
    public_key = '918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    pageNo = 1
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={public_key}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    # 웹스크래핑 requests
    response = requests.get(url)
    print("공공데이터 : ",response.text)  # str타입
    
    # 문자열 -> json타입으로 변경
    json_data = json.loads(response.text)
    list = json_data['response']['body']['items']['item'];
    print('json데이터 : ',json_data['response']['body']['items']['item'])     # json타입
    print('json데이터 1개 : ',json_data['response']['body']['items']['item'][0])
    context = {'list':list}
    return render(request,'pboard/list.html',context)
    