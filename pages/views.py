from django.views.generic import TemplateView

from accounts.models import CustomUser


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class PersonalPageView(TemplateView):
    model=CustomUser
    template_name = "pages/personal.html"


