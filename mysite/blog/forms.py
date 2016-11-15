from django import forms

class NewPostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField()
