from django.urls import path

from .views import HomePageView, PersonalPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("personal", PersonalPageView.as_view(), name="personal")
]
