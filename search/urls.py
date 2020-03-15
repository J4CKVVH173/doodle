from django.urls import path
from .views import search_page, search_result

urlpatterns = [
    path('search/', search_page),
    path('result/', search_result)
]
