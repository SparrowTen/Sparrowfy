from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# from youtubesearchpython import VideosSearch
import json
# import cardupdate



f = open('card.json', 'r')
CONTAINER = json.load(f)

def default(request):
    global CONTAINER

    song = 'kSFJGEHDCrQ'
    return render(request, 'player.html',{'CONTAINER':CONTAINER, 'song':song})

def login_auth(request):
    return render(request,'login.html')