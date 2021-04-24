from django.urls import path

from .views import home, about_us

urlpatterns = [
    # path('', index, name="index")
    path('', home, name="home"),
    path('about-us', about_us, name="about_us")
]
