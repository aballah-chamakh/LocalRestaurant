from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from . import api_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include(api_urls))
    path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh', refresh_jwt_token, name='token_refresh'),
]
]
if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
