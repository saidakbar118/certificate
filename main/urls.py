from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),  # /certificate/
    path('search/', views.search_view, name='search_view'),  # /certificate/search/
    path('<int:pk>/', views.detail_view, name='detail_view'),  # /certificate/1/
]
