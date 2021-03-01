from .models import *
from django import forms

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'


class RatingsForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields ='__all__'


