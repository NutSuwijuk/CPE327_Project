"""lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from One4All import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Category),
    path('Food', views.Food),
    path('category',views.Category),
    path('about',views.about),
    path('Location',views.Location),
    path('Number',views.Number),
    path('General/',views.General),        
    path('Person',views.Person),
    path('NormalLife',views.Normal),    

    #-------------person-----------------------
    path('me',views.me),
    path('you', views.you),
    path('she', views.she),
    path('we', views.we),
    path('they', views.they),
    path('dad', views.dad),
    path('mom', views.mom),
    path('baby', views.baby),
    path('man', views.man),
    path('woman', views.woman),
    path('grandfather', views.grandfather),
    path('grandmother', views.grandmother),
    path('grandfather2', views.grandfather2),
    path('grandmother2', views.grandmother2),
    path('uncle', views.uncle),
    path('aunt', views.aunt),
    path('aunt2', views.aunt2),
    path('aucle', views.aucle),
    path('grandchild', views.grandchild),
    path('oldbro', views.oldbro),
    path('youngbro', views.youngbro),
    path('oldsis', views.oldsis),
    path('youngsis', views.youngsis),
    path('child', views.child),
    path('teenager', views.teenager),
    path('adult', views.adult),
    path('elderly', views.elderly),
    path('monk', views.monk),

    
    #--------------General------------------
    path('General/กระทะ',views.กระทะ),
    path('General/เก้าอี้',views.เก้าอี้),
    path('General/จาน',views.จาน),  
    path('General/ช้อน',views.ช้อน),
    path('General/ตะหลิว',views.ตะหลิว),
    path('General/ตู้เย็น',views.ตู้เย็น), 
    path('General/ทัพพี',views.ทัพพี),
    path('General/แปรงสีฟัน',views.แปรงสีฟัน),
    
    #---------------Location------------------
    path('บ้าน',views.บ้าน),
    path('โรงเรียน',views.โรงเรียน),
    path('สถานีตำรวจ',views.สถานีตำรวจ),
    path('ตลาด',views.ตลาด),
    path('โรงพยาบาล',views.โรงพยาบาล),

    #---------------number-----------------
    path('A1บวก',views.A1บวก),
    path('A2ลบ',views.A2ลบ),
    path('A3คูณ',views.A3คูณ),
    path('A4หาร',views.A4หาร),
    path('A5เท่ากับ',views.A5เท่ากับ),
    path('N0',views.N0),
    path('N1',views.N1),
    path('N2',views.N2),
    path('N3',views.N3),
    path('N4',views.N4),
    path('N5',views.N5),
    path('N6',views.N6),
    path('N7',views.N7),
    path('N8',views.N8),
    path('N9',views.N9),
    path('N10',views.N10),
    path('N11',views.N11),
    path('N12',views.N12),
    path('N13',views.N13),
    path('N14',views.N14),
    path('N15',views.N15),
    path('N20',views.N20),
    path('N30',views.N30),
    path('N40',views.N40),
    path('N50',views.N50),
    path('N60',views.N60),
    path('N70',views.N70),
    path('N80',views.N80),
    path('N90',views.N90),
    path('N100',views.N100),
    path('N1000',views.N1000),

    #--------------------Food-------------------
    path('rice',views.rice),
    path('orange',views.orange),
    path('mango',views.mango),
    path('longan',views.longan),
    path('watermelon',views.watermelon),
    path('durian',views.durian),
    path('cucumber',views.cucumber),
    path('cabbage',views.cabbage),
    path('lettuce',views.lettuce),
    path('morning',views.morning),

    #------------------normal----------------------
    path('pay',views.pay),
    path('sorry',views.sorry),
    path('thank',views.thank),
    path('sad',views.sad),
    path('luck',views.luck),
    path('ill',views.ill),
    path('well',views.well),
    path('like',views.like),
    path('dislike',views.dislike),
    path('love',views.love),
    path('hungry',views.hungry),
    path('eat',views.eat),
    path('sleep',views.sleep),
    path('go',views.go),
    path('come',views.come),

]
