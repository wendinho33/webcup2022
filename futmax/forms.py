from django.forms import ModelForm
from futmax.models import FutUpload
from django.forms import ClearableFileInput


class FutForm(ModelForm):
    class Meta:
        model = FutUpload
        fields = ['title', 'images', 'scripts', 'price', 'payment', 'video']
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
            'scripts': ClearableFileInput(attrs={'multiple': True}),
        }