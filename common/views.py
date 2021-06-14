from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from urllib.request import Request, urlopen
from urllib.parse import unquote, urlencode, quote_plus
import requests
import xml.etree.ElementTree as elemTree

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
    공공데이터 api 가져오기
    """
    serviceUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
    serviceKey = 'ffxl4VMnlHEnjLKdDw2uaUS%2BPXvEczJ2mROokL5mf4n4mvo%2Face3eraz6GHHH%2FlEEeWYdcpVp7JVhbEkzsS6PA%3D%3D'
    seviceKey_decode = unquote(serviceKey)

    numOfRows = '50'
    pageNo = '1'
    MobileOS = 'ETC'
    MobileApp = 'TourAPI3.0_Guide'
    listYN = 'Y'
    arrange = 'A'
    contentTypeId = '12'
    areaCode = '1'
    cat1 = 'A01'

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
            addr2 = element.find('addr2') # 상세주소
            createdtime = element.find('createdtime').text # 콘텐츠 최초 등록일
            firstimage = element.find('firestimage') # 원본 대표 이미지
            firstimage2 = element.find('firestimage2') # 썸네일 대표 이미지
   

            data = {"title":title, "addr1":addr1, "addr2":addr2, "createdtime":createdtime,
                    "firstimage":firstimage, "firstimage2":firstimage2}
            
            forestList.append(data)

    context = {'forestList' : forestList}
    print(forestList)
    return render(request,'common/forest.html',context)
