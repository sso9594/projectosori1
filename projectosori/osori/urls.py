"""osori URL Configuration

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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from osoriapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('anonyboard.html', views.annonyboard,name='annoyboard'),
    path('fashionboard.html', views.fashionboard,name='fashionboard'),
    path('postcreate', views.postcreate,name='postcreate'),
    path('detail/<int:post_id>', views.detail,name='detail'),
    path('new_comment/<int:post_id>', views.new_comment,name='new_comment'),
    path('freepostcreate', views.freepostcreate,name='freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail,name='freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment,name='new_freecomment'),
    path('login.html', views.login, name='login'),
    path('logout.html', views.logout, name='logout'),
    path('register.html', views.register, name='register'),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
