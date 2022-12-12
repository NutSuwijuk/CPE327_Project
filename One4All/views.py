from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from django.db import connection
from One4All.models import *

from django.db import connection
from django.http import JsonResponse

from .models import Video
from .models import Person

# all_video = [
#     {'id': 1, 'title': 'เก้าอี้'},
#     {'id': 2, 'title': 'กระทะ'}
# ]

def CursorToDict(data,columns):
    result = []
    fieldnames = [name.replace(" ", "_").lower() for name in columns]
    for row in data:
        rowset = []
        for field in zip(fieldnames, row):
            rowset.append(field)
        result.append(dict(rowset))
    return result

def video(request):
    #Query Data
    # all_video = Video.objects.all()
    all_video = Video.objects.order_by('id')
    context = {'video': all_video}
    return render(request, 'general.html', context)

def person(request):
    #Query Data
    # all_video = Video.objects.all()
    all_video = Person.objects.order_by('no')
    context = {'person': all_video}
    return render(request, 'person.html', context)
#--------------------Create your views here.----------------------

def Category(request):
    return render(request, 'category.html')

def about(request):
    return render(request, 'about.html')

def Food(request):
    return render(request, 'food.html')

def Location(request):
    return render(request, 'location.html')

def Number(request):
    return render(request, 'number.html')         

# def General(request):
#     all_video = General.objects.order_by('id')
#     context = {'video': all_video}
#     return render(request, 'general.html', context)

    # return render(request, 'general.html')     

def Person(request):
    return render(request, 'person.html') 

def Normal(request):
    return render(request, 'normal.html')   

def กระทะ(request):
    return render(request, 'general/กระทะ.html') 

def เก้าอี้(request):
    return render(request, 'general/เก้าอี้.html') 

def จาน(request):
    return render(request, 'general/จาน.html') 

def ช้อน(request):
    return render(request, 'general/ช้อน.html') 

def ตะหลิว(request):
    return render(request, 'general/ตะหลิว.html') 

def ตู้เย็น(request):
    return render(request, 'general/ตู้เย็น.html') 

def ทัพพี(request):
    return render(request, 'general/ทัพพี.html') 

def แปรงสีฟัน(request):
    return render(request, 'general/แปรงสีฟัน.html') 

def ไม้กวาด(request):
    return render(request, 'general/ไม้กวาด.html') 

def ไม้ถูพื้น(request):
    return render(request, 'general/ไม้ถูพื้น.html') 

def ยาสีฟัน(request):
    return render(request, 'general/ยาสีฟัน.html') 

def รองเท้า(request):
    return render(request, 'general/รองเท้า.html') 

def สบู่(request):
    return render(request, 'general/สบู่.html') 

def ส้อม(request):
    return render(request, 'general/ส้อม.html') 

def หม้อ(request):
    return render(request, 'general/หม้อ.html')

#location
def บ้าน(request):
    return render(request, 'location/บ้าน.html')

def โรงเรียน(request):
    return render(request, 'location/โรงเรียน.html')

def สถานีตำรวจ(request):
    return render(request, 'location/สถานีตำรวจ.html')

def ตลาด(request):
    return render(request, 'location/ตลาด.html')

def โรงพยาบาล(request):
    return render(request, 'location/โรงพยาบาล.html')


# สำหรับเทส 
def test(request):
    return render(request, 'test_Category.html')