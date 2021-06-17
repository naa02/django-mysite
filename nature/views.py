from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .forms import Comment2Form
from urllib.request import Request, urlopen
from urllib.parse import unquote, urlencode, quote_plus
import xml.etree.ElementTree as elemTree
import requests
from .models import Comment2


def forest0(request):
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
            contentid = element.find('contentid').text # 컨텐트 id값
            
            data = {"contentid":contentid, "title":title, "addr1":addr1, "addr2 ":addr2, "firstimage":firstimage}

            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList)

    return render(request,'nature/forest0.html',context)

def forest1(request):
    """
    인천의 자연관광지 api 연천
    """
    serviceUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    serviceKey = 'ffxl4VMnlHEnjLKdDw2uaUS%2BPXvEczJ2mROokL5mf4n4mvo%2Face3eraz6GHHH%2FlEEeWYdcpVp7JVhbEkzsS6PA%3D%3D'
    seviceKey_decode = unquote(serviceKey)

    numOfRows = '40' # 한 페이지 결과 수
    pageNo = '1' # 페이지 번호
    MobileOS = 'ETC' # OS 구분
    MobileApp = 'TourAPI3.0_Guide' # 서비스명
    listYN = 'Y' # 목록 구분
    arrange = 'B' # 정렬 구분 (A=제목순, B=조회순, C=수정일순, D=생성일순, E=거리순)
    contentTypeId = '12' # 관광타입(관광지)
    areaCode = '2' # 지역코드(인천)
    cat1 = 'A01' # 대분류(자연천

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
            try:
                firstimage = element.find('firstimage').text # 원본 대표 이미지
            except Exception as e:
                continue
            contentid = element.find('contentid').text # 컨텐트 id값

            data = {"contentid":contentid, "title":title, "addr1":addr1, "addr2 ":addr2, "firstimage":firstimage}

            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList)
    return render(request,'nature/forest1.html',context)

def forest2(request):
    """
    경기도의 자연관광지 api 연동
    """
    serviceUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    serviceKey = 'ffxl4VMnlHEnjLKdDw2uaUS%2BPXvEczJ2mROokL5mf4n4mvo%2Face3eraz6GHHH%2FlEEeWYdcpVp7JVhbEkzsS6PA%3D%3D'
    seviceKey_decode = unquote(serviceKey)

    numOfRows = '40' # 한 페이지 결과 수
    pageNo = '1' # 페이지 번호
    MobileOS = 'ETC' # OS 구분
    MobileApp = 'TourAPI3.0_Guide' # 서비스명
    listYN = 'Y' # 목록 구분
    arrange = 'B' # 정렬 구분 (A=제목순, B=조회순, C=수정일순, D=생성일순, E=거리순)
    contentTypeId = '12' # 관광타입(관광지)
    areaCode = '31' # 지역코드(경기도)
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
            try:
                firstimage = element.find('firstimage').text # 원본 대표 이미지
            except Exception as e:
                continue
            contentid = element.find('contentid').text # 컨텐트 id값

            data = {"contentid":contentid, "title":title, "addr1":addr1, "addr2 ":addr2, "firstimage":firstimage}

            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList)
    return render(request,'nature/forest2.html',context)

def forest3(request):
    """
    강원도의 자연관광지 api 연동
    """
    serviceUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    serviceKey = 'ffxl4VMnlHEnjLKdDw2uaUS%2BPXvEczJ2mROokL5mf4n4mvo%2Face3eraz6GHHH%2FlEEeWYdcpVp7JVhbEkzsS6PA%3D%3D'
    seviceKey_decode = unquote(serviceKey)

    numOfRows = '40' # 한 페이지 결과 수
    pageNo = '1' # 페이지 번원
    MobileOS = 'ETC' # OS 구분
    MobileApp = 'TourAPI3.0_Guide' # 서비스명
    listYN = 'Y' # 목록 구분
    arrange = 'B' # 정렬 구분 (A=제목순, B=조회순, C=수정일순, D=생성일순, E=거리순)
    contentTypeId = '12' # 관광타입(관광지)
    areaCode = '32' # 지역코드(강원도)
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
            try:
                firstimage = element.find('firstimage').text # 원본 대표 이미지
            except Exception as e:
                continue
            contentid = element.find('contentid').text # 컨텐트 id값

            data = {"contentid":contentid, "title":title, "addr1":addr1, "addr2 ":addr2, "firstimage":firstimage}

            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList)
    return render(request,'nature/forest3.html',context)

def forest4(request):
    """
    부산의 자연관광지 api 연동
    """
    serviceUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    serviceKey = 'ffxl4VMnlHEnjLKdDw2uaUS%2BPXvEczJ2mROokL5mf4n4mvo%2Face3eraz6GHHH%2FlEEeWYdcpVp7JVhbEkzsS6PA%3D%3D'
    seviceKey_decode = unquote(serviceKey)

    numOfRows = '40' # 한 페이지 결과 수
    pageNo = '1' # 페이지 번호
    MobileOS = 'ETC' # OS 구분
    MobileApp = 'TourAPI3.0_Guide' # 서비스명
    listYN = 'Y' # 목록 구분
    arrange = 'B' # 정렬 구분 (A=제목순, B=조회순, C=수정일순, D=생성일순, E=거리순)
    contentTypeId = '12' # 관광타입(관광지)
    areaCode = '6' # 지역코드(산산)
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
            try:
                firstimage = element.find('firstimage').text # 원본 대표 이미지
            except Exception as e:
                continue
            contentid = element.find('contentid').text # 컨텐트 id값

            data = {"contentid":contentid, "title":title, "addr1":addr1, "addr2 ":addr2, "firstimage":firstimage}

            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList)
    return render(request,'nature/forest4.html',context)
    
def forest5(request):
    """
    제주도의 자연관광지 api 연동
    """
    serviceUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    serviceKey = 'ffxl4VMnlHEnjLKdDw2uaUS%2BPXvEczJ2mROokL5mf4n4mvo%2Face3eraz6GHHH%2FlEEeWYdcpVp7JVhbEkzsS6PA%3D%3D'
    seviceKey_decode = unquote(serviceKey)

    numOfRows = '40' # 한 페이지 결과 수
    pageNo = '1' # 페이지 번호
    MobileOS = 'ETC' # OS 구분
    MobileApp = 'TourAPI3.0_Guide' # 서비스명
    listYN = 'Y' # 목록 구분
    arrange = 'B' # 정렬 구분 (A=제목순, B=조회순, C=수정일순, D=생성일순, E=거리순)
    contentTypeId = '12' # 관광타입(관광지)
    areaCode = '39' # 지역코드(제주도)
    cat1 = 'A01' # 대분류(자연)

    parameters = {"serviceKey":seviceKey_decode, "numOfRows" : numOfRows, "pageNo" : pageNo,
                    "MobileOS" : MobileOS, "MobileApp" : MobileApp, "listYN" : listYN, 
                    "arrange" : arrange, "contentTypeId" : contentTypeId, "areaCode" : areaCode,
                    "cat1" : cat1 }
    response = requests.get(serviceUrl, params=parameters)

    print(response.text) # XML로 가져옴

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
            try:
                firstimage = element.find('firstimage').text # 원본 대표 이미지
            except Exception as e:
                continue
            contentid = element.find('contentid').text # 컨텐트 id값

            data = {"contentid":contentid, "title":title, "addr1":addr1, "addr2 ":addr2, "firstimage":firstimage}

            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList) # List에 넣어서 출력
    return render(request,'nature/forest5.html',context)

# @login_required(login_url='common:login')
# def comment2_create(request, comment2_id):
#     """
#     장소에 대한 comment 등록하기
#     """
#     forest = get_object_or_404(Forest, pk=comment2_id)
#     if request.method == "POST":
#         form = Comment2Form(request.POST)
#         if form.is_valid():
#             comment2 = form.save(commit=False)
#             comment2.author = request.user  # 추가한 속성 author 적용
#             comment2.create_date = timezone.now()
#             comment2.save()
#             return redirect('{}#comment2_{}'.format(
#                 resolve_url('common:comment2', comment2_id=forest.id)))
#     else:
#         form = Comment2Form()
#     context = {'form': form}
#     return render(request, 'common/review_form.html', context)

def index2(request, comment2_id):
    """
    comment 목록 출력
    """
    comment2 = get_object_or_404(Comment2, pk=comment2_id)
    context = {'comment2': comment2}
    return render(request, 'nature/review_detail.html', context)


@login_required(login_url='common:login')
def comment2(request, comment2_id):
    """
    장소에 대한 comment 보여주기
    """
    print
    comment2 = get_object_or_404(Comment2, pk=comment2_id)
    if request.method == 'POST':
        form = Comment2Form(request.POST)
        if form.is_valid():
            comment2 = form.save(commit=False)
            comment2.author = request.user  # 추가한 속성 author 적용
            comment2.create_date = timezone.now()
            comment2.save()
            return redirect('{}#comment2_{}'.format(
                resolve_url('nature:index', comment2_id=comment2.id)))
    else:
        form = Comment2Form()
    context = {'form': form}
    return render(request, 'nature/review_detail.html', context)
