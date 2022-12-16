from django.urls import path
from level4 import views


app_name='level4'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
