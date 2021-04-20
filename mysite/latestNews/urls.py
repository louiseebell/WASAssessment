from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='home'),
    path('News/<int:pk>', views.NewsDetailView.as_view(), name='detail'),
]