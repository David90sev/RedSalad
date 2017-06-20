from django import forms


class ProductorForm(forms.Form):
    alias_empresa = forms.CharField(max_length=60)
    bio = forms.CharField(widget=forms.Textarea,max_length=500)
    