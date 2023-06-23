from django import forms
from catalog.models import FashionBlog


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = FashionBlog
        exclude = ('slug', 'created_at', 'view_count',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        }








