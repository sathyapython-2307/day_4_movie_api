# ...existing code...
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Welcome to the Movie API!</h2><p>Visit <a href="/api/movies/">Movies</a>.</p>')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
