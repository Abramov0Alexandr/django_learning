from django import forms
from catalog.models import FashionBlog


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = FashionBlog
        fields = ('title', 'slug', 'content', 'image', 'is_published',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        }
