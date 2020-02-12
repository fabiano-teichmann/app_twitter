from django import forms

from core.models import Hashtag


class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ('hashtag', )
        widgets = {
            'hashtag': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'arial-label': 'hash tag'})
        }
