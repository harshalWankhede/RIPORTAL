"""RIM_PORTAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .import views
#from .views import CreatePostView

urlpatterns=[
    path("",views.index,name="index"),
#path("upload",views.upload,name="upload"),
#path('upload/', CreatePostView.as_view(), name='add_post'),
path('upload/', views.upload, name='upload'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search1/$', views.search1,name='search1'),
    url(r'^approved/$', views.approved,name='approved'),
    url(r'^unapproved/$', views.unapproved,name='unapproved'),
    url(r'^RimErrors/$', views.RimErrors,name='RimErrors'),
]
