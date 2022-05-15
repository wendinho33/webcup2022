from django.forms import ModelForm
from futmax.models import FutUpload, Contact


class FutForm(ModelForm):
    class Meta:
        model = FutUpload
        fields = ['title', 'images', 'price', 'payment', 'video', 'method']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']