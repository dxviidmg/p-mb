"""p_mb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# To serve files during dev
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from proveedores import views as proveedores_views
from articulos import views as articulos_views
from clientes import views as clientes_views
from pedidos import views as pedidos_views

router = routers.DefaultRouter()
router.register(r'proveedores', proveedores_views.ProveedorViewSet)
router.register(r'articulos', articulos_views.ArticuloViewSet)
router.register(r'clientes', clientes_views.ClienteViewSet)
router.register(r'pedidos', pedidos_views.PedidoViewSet, basename='pedido')
router.register(r'dashboard', pedidos_views.DashboardViewSet, basename="dashboard")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)