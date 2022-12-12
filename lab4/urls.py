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
    path('General/',views.videos),        
    path('Person',views.Person),
    path('NormalLife',views.Normal),    
    path('General/<str:video_title>', views.video),

    #person--------------------------------------------
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

    
    # General
    path('กระทะ',views.กระทะ),
    path('เก้าอี้',views.เก้าอี้),
    path('จาน',views.จาน),  
    path('ช้อน',views.ช้อน),
    path('ตะหลิว',views.ตะหลิว),
    path('ตู้เย็น',views.ตู้เย็น), 
    path('ทัพพี',views.ทัพพี),
    path('แปรงสีฟัน',views.แปรงสีฟัน),
    path('ไม้กวาด',views.ไม้กวาด), 
    path('ไม้ถูพื้น',views.ไม้ถูพื้น),
    path('ยาสีฟัน',views.ยาสีฟัน),
    path('รองเท้า',views.รองเท้า),  
    path('สบู่',views.สบู่),
    path('ส้อม',views.ส้อม),
    path('หม้อ',views.หม้อ),
    
    #Location
    path('บ้าน',views.บ้าน),
    path('โรงเรียน',views.โรงเรียน),
    path('สถานีตำรวจ',views.สถานีตำรวจ),
    path('ตลาด',views.ตลาด),
    path('โรงพยาบาล',views.โรงพยาบาล),

    #number
    path('A1บวก',views.A1บวก),
    path('A2ลบ',views.A2ลบ),
    path('A3คูณ',views.A3คูณ),
    path('A4หาร',views.A4หาร),
    path('A5เท่ากับ',views.A5เท่ากับ),
    path('0',views.N0),
    path('1',views.N1),
    path('2',views.N2),
    path('3',views.N3),
    path('4',views.N4),
    path('5',views.N5),
    path('6',views.N6),
    path('7',views.N7),
    path('8',views.N8),
    path('9',views.N9),
    path('10',views.N10),
    path('11',views.N11),
    path('12',views.N12),
    path('13',views.N13),
    path('14',views.N14),
    path('15',views.N15),
    path('20',views.N20),
    path('30',views.N30),
    path('40',views.N40),
    path('50',views.N50),
    path('60',views.N60),
    path('70',views.N70),
    path('80',views.N80),
    path('90',views.N90),
    path('100',views.N100),
    path('500',views.N500),
    path('1000',views.N1000),

    #Food
    path('ข้าว',views.ข้าว),


]
