from django.contrib import admin
from django.urls import path, include
from api.views import ListCreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/user/register', ListCreateUserView.as_view(), name='create-user'),
    path('api/token/', TokenObtainPairView.as_view(), name='get-token'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='refresh-token'),
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
