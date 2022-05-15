from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from futmax.models import FutUpload, Contact
from futmax.forms import FutForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from django.urls import reverse_lazy


# Create your views here.

def futindex(request):
    return render(request, 'futmax/index.html')


def pricing(request):
    return render(request, 'futmax/pricing.html')


class ThankView(LoginRequiredMixin, TemplateView):
    login_url = '/user/'
    template_name = 'futmax/thank.html'


class FutCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/user/'
    form_class = FutForm
    template_name = 'futmax/create.html'
    success_url = reverse_lazy('thank_you')
    success_message = 'LE LIEN DE PAIEMENT VOUS SERA ENVOYEZ DANS VOTRE MAIL'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FutListView(LoginRequiredMixin, ListView):
    login_url = '/user/'
    model = FutUpload
    template_name = 'futmax/list.html'
    queryset = FutUpload.objects.all()
    context_object_name = 'futs'


class FutDetailView(LoginRequiredMixin, DetailView):
    login_url = '/user/'
    model = FutUpload
    template_name = 'futmax/detail.html'
    queryset = FutUpload.objects.all()
    context_object_name = 'fut'


class ContactView(SuccessMessageMixin, CreateView):
    model = ContactForm
    form_class = ContactForm
    template_name = 'futmax/contact.html'
    success_url = reverse_lazy('home')
    success_message = 'MAIL ENVOYEZ, FUTMAX VAS REVENIR VERS VOUS'
