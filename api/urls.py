from django.urls import path, include, re_path
from .views import index
from django.views.generic import TemplateView
from django.contrib.gis import admin
from world.views import CampSpotsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/', index, name='index'),
    path('auth/', include('authapp.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('spot/', CampSpotsView.as_view(), name='test')

]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
