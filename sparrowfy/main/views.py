from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from youtubesearchpython import VideosSearch
import json
import requests
# import cardupdate
import os

workdir = os.path.dirname(__file__).split('main')[0] + '/'
f = open(workdir + 'card.json', 'r')
CONTAINER = json.load(f)

def default(request):
    global CONTAINER

    song = 'kSFJGEHDCrQ'
    return render(request, 'player.html',{'CONTAINER':CONTAINER, 'song':song})

@csrf_exempt
def login_auth(request):
    return render(request,'login.html')

def main_page(request):
    r = requests.get('http://127.0.0.1:5500/api/song/getPlayList?artist=Ayase / YOASOBI')
    YOASOBI = json.loads(r.text)
    r = requests.get('http://127.0.0.1:5500/api/song/getPlayList?artist=Ado')
    Ado = json.loads(r.text)
    return render(request,"mainpage.html",{'YOASOBI': YOASOBI,'Ado':Ado})

@csrf_exempt
def signup(request):
    return render(request,'signup.html')

@csrf_exempt
def signupsubmit(request):
        if request.method=="POST":
            name=request.POST['name']
            password = request.POST['password']
            data = {
                 'name':name,
                 'password':password
            }
            r = requests.post('http://127.0.0.1:5500/api/auth/register',data=data)
            print(r.text)
            return redirect('/login')
        return redirect('/signup')

@csrf_exempt
def loginsubmit(request):
      if request.method=="POST":
            name=request.POST['name']
            password = request.POST['password']
            data = {
                 'name':name,
                 'password':password
            }
            r = requests.post('http://127.0.0.1:5500/api/auth/login',data=data)
            print(r.text)
            return redirect('/main')