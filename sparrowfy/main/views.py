from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# from youtubesearchpython import VideosSearch
import json
import requests
# import cardupdate



f = open('card.json', 'r')
CONTAINER = json.load(f)

def default(request):
    global CONTAINER

    song = 'kSFJGEHDCrQ'
    return render(request, 'player.html',{'CONTAINER':CONTAINER, 'song':song})

def login_auth(request):
    return render(request,'login.html')

def main_page(request):
    r = requests.get('http://127.0.0.1:5500/api/song/getPlayList?artist=Ayase / YOASOBI')
    YOASOBI = json.loads(r.text)
    r = requests.get('http://127.0.0.1:5500/api/song/getPlayList?artist=Ado')
    Ado = json.loads(r.text)
    return render(request,"mainpage.html",{'YOASOBI': YOASOBI,'Ado':Ado})

def signup(request):
    return render(request,'signup.html')