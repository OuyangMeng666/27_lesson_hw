
from django.contrib import admin
from django.urls import path, include

from ads import views

urlpatterns = [
    path('', views.root),
    path('admin/', admin.site.urls),
    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
    path('ad/create', views.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/update_image', views.AdUploadImageView.as_view()),
    path('user/', include('users.urls'))
]
