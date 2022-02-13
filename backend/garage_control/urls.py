from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('api/', include(doc_urls)),
    path('admin/', admin.site.urls),
]
