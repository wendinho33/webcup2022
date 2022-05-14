from django.shortcuts import render
from django.views.generic import CreateView
from futmax.models import FutUpload
from futmax.forms import FutForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def futindex(request):
    return render(request, 'futmax/index.html')


def pricing(request):
    return render(request, 'futmax/pricing.html')


class FutCreateView(CreateView, LoginRequiredMixin):
    login_url = 'login'
    form_class = FutForm
    template_name = 'futmax/create.html'
    success_url = 'thank_you'
