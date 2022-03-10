
from django.contrib import admin
from django.urls import path

from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat/', views.CategoryView.as_view()),
    path('add_info_ads', views.add_info_ads.as_view()),
    path('add_info_cats', views.add_info_cat.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>', views.AdDetailViews.as_view()),
]
