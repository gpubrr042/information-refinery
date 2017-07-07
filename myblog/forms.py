from django import forms



class RequestForm(forms.Form):
    name = forms.CharField(required=True)
    topic = forms.CharField(required=True)
    details = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    