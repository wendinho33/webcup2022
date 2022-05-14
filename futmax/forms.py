from django.forms import ModelForm
from futmax.models import FutUpload


class FutForm(ModelForm):
    class Meta:
        model = FutUpload
        fields = ['title', 'images', 'price', 'payment', 'video', 'method']
