from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from urllib.request import Request, urlopen
from urllib.parse import unquote, urlencode, quote_plus
import requests
import xml.etree.ElementTree as elemTree
from .models import Forest, Review
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def forest(request):
    """
    서울의 자연관광지 api 연동
    """
    serviceUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    serviceKey = 'ffxl4VMnlHEnjLKdDw2uaUS%2BPXvEczJ2mROokL5mf4n4mvo%2Face3eraz6GHHH%2FlEEeWYdcpVp7JVhbEkzsS6PA%3D%3D'
    seviceKey_decode = unquote(serviceKey)

    numOfRows = '30' # 한 페이지 결과 수
    pageNo = '1' # 페이지 번호
    MobileOS = 'ETC' # OS 구분
    MobileApp = 'TourAPI3.0_Guide' # 서비스명
    listYN = 'Y' # 목록 구분
    arrange = 'B' # 정렬 구분 (A=제목순, B=조회순, C=수정일순, D=생성일순, E=거리순)
    contentTypeId = '12' # 관광타입(관광지)
    areaCode = '1' # 지역코드(서울)
    cat1 = 'A01' # 대분류(자연)

    parameters = {"serviceKey":seviceKey_decode, "numOfRows" : numOfRows, "pageNo" : pageNo,
                    "MobileOS" : MobileOS, "MobileApp" : MobileApp, "listYN" : listYN, 
                    "arrange" : arrange, "contentTypeId" : contentTypeId, "areaCode" : areaCode,
                    "cat1" : cat1 }
    response = requests.get(serviceUrl, params=parameters)

    print(response.text)

    forestList=[]
    
    if response.status_code == 200:
        tree = elemTree.fromstring(response.text)
        iter = tree.iter(tag="item")

        for element in iter:
            title = element.find('title').text # 제목
            addr1 = element.find('addr1').text # 주소
            try:
                addr2 = element.find('addr2').text # 상세주소
            except Exception as e:
                continue
            firstimage = element.find('firstimage').text # 원본 대표 이미지
   
            data = {"title":title, "addr1":addr1, "addr2 ":addr2, "firstimage":firstimage}

            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList)
    return render(request,'common/forest.html',context)

@login_required(login_url='common:login')
def review(request):
    """
    review 등록
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('pybo:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'common/review_detail.html', context)