"""
URL configuration for DiseasesInfo project.

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
from django.conf import settings
from django.conf.urls.static import static
from App import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('search/login/', views.loginPage, name='login'),
    path('/', views.home, name='home'),
    path('search/',views.search,name='search'),
    path('search1/',views.search1,name='search1'),
    path('search2/',views.search2,name='search2'),
    path('search3/',views.search3,name='search3'),
    path('search4/',views.search4,name='search4'),
    path('dash2/', views.dash2, name='dash2'),
    path('dash4/', views.dash4, name='dash4'),
    path('dash5/', views.dash5, name='dash5'),
    path('dash6/', views.dash6, name='dash6'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)