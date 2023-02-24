from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('tinymce/', include('tinymce.urls')),
]