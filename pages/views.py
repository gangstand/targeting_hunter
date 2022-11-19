import os

from django.shortcuts import render
from django.views.generic import TemplateView
import qrcode
from accounts.models import CustomUser


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class PersonalPageView(TemplateView):
    model = CustomUser
    template_name = "pages/personal.html"

    def get(self, request, *args, **kwargs):
        name = 'TargetHunteruser_id'
        path = f'media\\TargetHunteruser_id_{request.user.id}.png'
        if request.method == 'GET' and request.user.is_authenticated:
            if not os.path.exists(path):
                img = qrcode.make(f'{name}{request.user.id}')
                img.save(path)
                CustomUser.objects.update(card=path)
        return render(request, 'pages/personal.html', {"path": path})
