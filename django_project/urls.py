from django.contrib import admin
from django.urls import path, include


urlpatterns = [
path('admin/', admin.site.urls),
#connect path to hockey_app urls
path('', include('hockey_app.urls')),
]
