from django.urls import path
from blog.views import index_page

urlpatterns = [
    path('', index_page)
]