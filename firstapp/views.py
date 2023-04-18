import requests
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

from .models.news import News

import datetime

# Create your views here.
def home(request):
    data = News.objects.all()
    data = list(data)
    #latest news first (filter)
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if int(data[j].id) <int(data[j+1].id):
                data[j],data[j+1]=data[j+1],data[j]
    data = data[:5]
    total_obj = News.objects.count()
    return render(request,'home.html',{"context":data,"total_obj":total_obj})

def help(request):
    return render(request,'help.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def details(request,id):
    data2 = News.objects.all()
    data = News.objects.get(id=id)
    created_hr = data.time.hour
    current_hr = datetime.datetime.now().hour
    dif = int(current_hr)-int(created_hr)
    diff=""
    if dif == 0:
        diff = " hour ago"
    else:
        diff = str(dif)+" hours ago"
    related_news=[]
    total_data = News.objects.all()
    for i in total_data:
        if i.category == data.category and i.id != id :
            related_news.append(i)



    return render(request,'details.html',{"context":data,"t":diff,"related_news":related_news,"context2":data2 })

def load_more(request):
    total_itm = int(request.GET.get('total_item'))
    limit = 2
    post_obj = list(News.objects.values())
    
    for i in range(len(post_obj)):
        for j in range(len(post_obj)-i-1):
                if post_obj[j]["id"] < post_obj[j+1]["id"]:
                    post_obj[j],post_obj[j+1]=post_obj[j+1],post_obj[j]
            
    post_obj=post_obj[total_itm:total_itm+limit]
    data = {
        'posts':post_obj
    }
    
    return JsonResponse(data=data)


def load_Sports(request):   
    total_datas = list(News.objects.values().filter(category="Sports"))
    
    data = {
        "news":total_datas
        }
    
    return JsonResponse(data=data)


def load_Politics(request):
    total_datas = list(News.objects.values().filter(category="Politics"))
    
    data = {
        "news":total_datas
        }
    
    return JsonResponse(data=data)


def load_Business(request):
    total_datas = list(News.objects.values().filter(category="Business"))
    data = {
        "news":total_datas
        }
    return JsonResponse(data=data)

def load_Crime(request):
    total_datas = list(News.objects.values().filter(category="Crime"))
    data = {
        "news":total_datas
        }
    return JsonResponse(data=data)

def load_Entertainment(request):
    total_datas = list(News.objects.values().filter(category="Entertainment"))
    data = {
        "news":total_datas
        }
    return JsonResponse(data=data)

def load_International(request):
    total_datas = list(News.objects.values().filter(category="International"))
    data = {
        "news":total_datas
        }
    return JsonResponse(data=data)



def loadSearch(request):
    query = request.GET['query']
    data = News.objects.filter(title__icontains=query)
    return render(request,'search.html',{"context":data}) 