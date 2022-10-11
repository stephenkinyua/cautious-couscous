
from django.contrib import admin
from django.urls import path, include
from users.views import CustomObtainAuthTokenView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('token-login/', CustomObtainAuthTokenView.as_view(), name='api_token_auth'), 
    path('register/', RegisterView.as_view(), name='auth_register'),

    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]
