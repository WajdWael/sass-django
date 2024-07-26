from django.contrib import admin
from django.urls import path

from .views import home_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', home_page_view),
    path('hello-world.html', home_page_view),
    path("", home_page_view),
]