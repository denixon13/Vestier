from appvestier import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('politica/', views.politica, name='politica'),  # Politica page view
    path('products/', include('products.urls')),  # Include products app URLs
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('orders/', include('orders.urls')),  # Include orders app URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)