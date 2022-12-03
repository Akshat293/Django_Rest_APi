from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>', views.ProductMixnView.as_view(),name='product-detail'),
    path('<int:pk>/update/', views.ProductMixnView.as_view(),name='product-update'),
    path('<int:pk>/delete/', views.ProductMixnView.as_view()),
    path('', views.ProductListCreateAPIView.as_view(),name='product-list')
]
