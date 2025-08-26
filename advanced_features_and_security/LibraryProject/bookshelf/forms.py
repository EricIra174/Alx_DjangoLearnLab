from django import forms
from .models import Book

# Secure form for creating or editing a Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # Adjust fields as per your model

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Example sanitization logic
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid characters in title")
        return title
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')