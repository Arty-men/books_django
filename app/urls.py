from django.contrib import admin
from django.urls import include, path 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('books', include('books.urls', namespace='books')),
    
    
]
