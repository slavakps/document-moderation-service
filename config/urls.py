from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from documents.views import UserRegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('documents.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/', obtain_auth_token, name='api-token'),
    path('api/register/', UserRegisterView.as_view(), name="register"),
]
