
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('register/', include('register_pages.urls')),
    path('login/', include('login_page.urls')),
]
