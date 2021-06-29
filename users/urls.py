from django.urls import path
from .views import BlacklistTokenUpdateView, CustomUserCreate

app_name = 'users'

urlpatterns = [
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('register/', CustomUserCreate.as_view(), name="create_user"),
]