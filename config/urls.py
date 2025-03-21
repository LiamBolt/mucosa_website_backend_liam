"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
from core.admin import admin_site
from django.urls import path, include


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('mucosa_secret/admin/', admin_site.urls),
    # path('', include('apps.home.urls')),
    path('partners/', include('apps.partners.urls')),
    path('news/', include('apps.news.urls')),
    path('events/', include('apps.events.urls')),
    path('projects/', include('apps.projects.urls')),
    path('career/', include('apps.career.urls')),
    path('about/', include('apps.about.urls')),
]
