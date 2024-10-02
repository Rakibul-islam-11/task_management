from django import forms
from category.models import creat_category

class creat_form(forms.ModelForm):
    class Meta:
        model=creat_category
        fields='__all__'