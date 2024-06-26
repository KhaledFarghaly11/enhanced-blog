from django import forms
from .models import Comment

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['name', 'email', 'body']