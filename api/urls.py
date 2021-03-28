from django.urls import path, include, re_path
from .views import index
from django.views.generic import TemplateView
from django.contrib.gis import admin
from world.views import CampSpotsView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/', index, name='index'),
    path('auth/', include('authapp.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('spot/', CampSpotsView.as_view(), name='test')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#= [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))] 
