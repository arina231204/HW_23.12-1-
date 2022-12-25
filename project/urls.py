
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from company import views

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet),
router.register('category', views.CategoryViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/company/', views.CompanyCreateListView.as_view()),
    path('api/company/<int:pk>/', views.CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('api/', include(router.urls)),
]
