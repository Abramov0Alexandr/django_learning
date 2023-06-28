from django import forms
from blog.models import FashionBlog


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = FashionBlog
        exclude = ('slug', 'created_at', 'view_count',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
            'is_published': forms.NullBooleanSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
