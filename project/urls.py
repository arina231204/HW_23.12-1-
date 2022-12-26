
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from company import views

# router = routers.DefaultRouter()
# router.register('product', views.ProductViewSet),
# router.register('category', views.CategoryViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', views.create_product),
    path('api/product/<int:pk>/', views.detail_product),
    path('api/company/', views.create_company),
    path('api/company/<int:pk>/', views.detail_company),
    path('api/category/', views.create_category),
    path('api/category/<int:pk>/', views.detail_category),
    # path('api/company/<int:pk>/', views.CompanyRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/', include(router.urls)),
]
