from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from django.db import connection
from One4All.models import *

from django.db import connection
from django.http import JsonResponse

from .models import Video

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

def videos(request):
    #Query Data
    # all_video = Video.objects.all()
    all_video = Video.objects.order_by('id')
    context = {'video': all_video}
    return render(request, 'general.html', context)

def video(request, video_title):
    #Query Data
    # all_video = Video.objects.all()
    one_video = Video.objects.get(title = video_title)
    context = {'video': one_video}
    return render(request, 'generals.html', context)


#--------------------Create your views here.----------------------

def Category(request):
    return render(request, 'category.html')

def about(request):
    return render(request, 'about.html')

def Food(request):
    return render(request, 'food.html')

def Location(request):
    return render(request, 'location.html')        

# def General(request):
#     all_video = General.objects.order_by('id')
#     context = {'video': all_video}
#     return render(request, 'general.html', context)

    # return render(request, 'general.html')   
  
#person ---------------------------------------
def Person(request):
    return render(request, 'person.html')

def me(request):
    return render(request, 'person/me.html')

def you(request):
    return render(request, 'person/you.html')

def she(request):
    return render(request, 'person/she.html')

def we(request):
    return render(request, 'person/we.html')

def they(request):
    return render(request, 'person/they.html')

def dad(request):
    return render(request, 'person/dad.html')

def mom(request):
    return render(request, 'person/mom.html')

def baby(request):
    return render(request, 'person/baby.html')

def man(request):
    return render(request, 'person/man.html')

def woman(request):
    return render(request, 'person/woman.html')

def grandfather(request):
    return render(request, 'person/grandfather.html')

def grandmother(request):
    return render(request, 'person/grandmother.html')

def grandfather2(request):
    return render(request, 'person/grandfather2.html')

def grandmother2(request):
    return render(request, 'person/grandmother2.html')

def uncle(request):
    return render(request, 'person/uncle.html')

def aunt(request):
    return render(request, 'person/aunt.html')

def aunt2(request):
    return render(request, 'person/aunt2.html')

def aucle(request):
    return render(request, 'person/aucle.html')

def grandchild(request):
    return render(request, 'person/grandchild.html')

def oldbro(request):
    return render(request, 'person/oldbro.html')

def youngbro(request):
    return render(request, 'person/youngbro.html')

def oldsis(request):
    return render(request, 'person/oldsis.html')

def youngsis(request):
    return render(request, 'person/youngsis.html')

def child(request):
    return render(request, 'person/child.html')

def teenager(request):
    return render(request, 'person/teenager.html')

def adult(request):
    return render(request, 'person/adult.html')

def elderly(request):
    return render(request, 'person/elderly.html')

def monk(request):
    return render(request, 'person/monk.html')

#normal------------------------------------------
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

#Food
def ข้าว(request):
    return render(request, 'food/ข้าว.html')

def ต้นข้าว(request):
    return render(request, 'food/ต้นข้าว.html')

#number
def Number(request):
    return render(request, 'number.html') 

def A1บวก(request):
    return render(request, 'numbers/A1บวก.html')

def A2ลบ(request):
    return render(request, 'numbers/A2ลบ.html')

def A3คูณ(request):
    return render(request, 'numbers/A3คูณ.html')

def A4หาร(request):
    return render(request, 'numbers/A4หาร.html')

def A5เท่ากับ(request):
    return render(request, 'numbers/A5เท่ากับ.html')

def N0(request):
    return render(request, 'numbers/0.html')

def N1(request):
    return render(request, 'numbers/1.html')

def N2(request):
    return render(request, 'numbers/2.html')

def N3(request):
    return render(request, 'numbers/3.html')

def N4(request):
    return render(request, 'numbers/4.html')

def N5(request):
    return render(request, 'numbers/5.html')

def N6(request):
    return render(request, 'numbers/6.html')

def N7(request):
    return render(request, 'numbers/7.html')

def N8(request):
    return render(request, 'numbers/8.html')

def N9(request):
    return render(request, 'numbers/9.html')

def N10(request):
    return render(request, 'numbers/10.html')

def N11(request):
    return render(request, 'numbers/11.html')

def N12(request):
    return render(request, 'numbers/12.html')

def N13(request):
    return render(request, 'numbers/13.html')

def N14(request):
    return render(request, 'numbers/14.html')

def N15(request):
    return render(request, 'numbers/15.html')

def N20(request):
    return render(request, 'numbers/20.html')

def N30(request):
    return render(request, 'numbers/30.html')

def N40(request):
    return render(request, 'numbers/40.html')

def N50(request):
    return render(request, 'numbers/50.html')

def N60(request):
    return render(request, 'numbers/60.html')

def N70(request):
    return render(request, 'numbers/70.html')

def N80(request):
    return render(request, 'numbers/80.html')

def N90(request):
    return render(request, 'numbers/90.html')

def N100(request):
    return render(request, 'numbers/100.html')

def N500(request):
    return render(request, 'numbers/500.html')

def N1000(request):
    return render(request, 'numbers/1000.html')
