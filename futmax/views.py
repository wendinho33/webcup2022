from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from futmax.models import FutUpload
from futmax.forms import FutForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy


# Create your views here.

def futindex(request):
    return render(request, 'futmax/index.html')


def pricing(request):
    return render(request, 'futmax/pricing.html')


class ThankView(LoginRequiredMixin, TemplateView):
    login_url = '/user/'
    template_name = 'futmax/thank.html'


class FutCreateView(LoginRequiredMixin, CreateView):
    login_url = '/user/'
    form_class = FutForm
    template_name = 'futmax/create.html'
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FutListView(LoginRequiredMixin, ListView):
    login_url = '/user/'
    model = FutUpload
    template_name = 'futmax/list.html'
    queryset = FutUpload.objects.all()


class FutDetailView(LoginRequiredMixin, DetailView):
    login_url = '/user/'
    model = FutUpload
    template_name = 'futmax/detail.html'
    queryset = FutUpload.objects.all()
    context_object_name = 'fut'