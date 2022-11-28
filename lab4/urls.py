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
from report import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Category),
    path('Food', views.Food),
    path('category',views.Category),
    path('about',views.about),
    path('Location',views.Location),
    path('Number',views.Number),
    path('General',views.General),        
    path('Person',views.Person),
    path('NormalLife',views.Normal),     
    
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
    
]
