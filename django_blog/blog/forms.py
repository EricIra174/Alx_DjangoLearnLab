from django import forms
from .models import Comment, Post
from taggit.forms import TagWidget
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Write your comment here...",
                "class": "form-control",
            }),
        }
        def clean_content(self):
            content = self.cleaned_data.get('content')
            if not content or content.strip() == "":
                raise forms.ValidationError("Comment content cannot be empty.")
            if len(content) > 500:
                raise forms.ValidationError("Comment content cannot exceed 500 characters.")
            return content
        

class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "tags": TagWidget(),
        }