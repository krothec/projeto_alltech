from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = 'Painel de Controle'
admin.AdminSite.site_title = 'AllTech'
admin.AdminSite.index_title = 'Painel de Controle'

