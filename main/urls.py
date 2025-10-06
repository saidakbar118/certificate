from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view),
    path("53c967b18b28db4c853278a5ccaa60ba/<int:pk>/", detail_view, name="detail"),
]