"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.global_settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat_server.views import ServerListViewSet

router = DefaultRouter()
router.register("api/server/select/", ServerListViewSet)
# router.register('data', ServerListViewSet)
# router.register(prefix='api', viewset='api/server/select', basename='category')
 
urlpatterns = [
    #in-build
    path('admin/', admin.site.urls),
 
    #portfolio VictorGrinan
    path('', include('VictorGrinan.urls')),

    #chat
] + router.urls

#setting images
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)