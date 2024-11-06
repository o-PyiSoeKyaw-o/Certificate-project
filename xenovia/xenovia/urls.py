"""
URL configuration for xenovia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from my_blog import views
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    path('',lambda request:redirect('/home')),
    path('admin/', admin.site.urls),
    path('home/', views.productList),
    path('home/create/',views.createProduct),
    path('home/detail/<int:product_id>/',views.productDetail),
    path('home/update/<int:product_id>/',views.productUpdate),
    path('home/delete/<int:product_id>/',views.productDelete),
    path('home/login/',views.loginView,name="login"),
    path('home/logout/',views.logoutView,name="logout"),
    path('home/cmt/create/<int:product_id>/',views.cmt_create),
    path('home/cmt/update/<int:cmt_id>/<int:product_id>/', views.cmt_update),
    path('home/cmt/delete/<int:cmt_id>/<int:product_id>/', views.cmt_delete),
    path('home/search_by/',views.search_by),
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
