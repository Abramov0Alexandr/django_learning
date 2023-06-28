from django import forms
from catalog.models import Product, Version

FORBIDDEN_WORDS = 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар'


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomNullBooleanSelect(forms.NullBooleanSelect):
    def __init__(self, attrs=None):
        choices = (
            ("unknown", "Не указано"),
            ("true", "Активна"),
            ("false", "Не активна"),
        )
        super().__init__(attrs=attrs)
        self.choices = choices


class CreateProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
            'image': forms.FileInput(),
            'price': forms.NumberInput()
        }

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in FORBIDDEN_WORDS.replace(', ', ' ').split():
            if word.lower() in cleaned_data.lower().split():
                raise forms.ValidationError('Обнаружены недопустимые слова в описании')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    is_active = forms.BooleanField(widget=CustomNullBooleanSelect, label='Признак активности')

    class Meta:
        model = Version
        fields = '__all__'
        widgets = {
            'version_title': forms.TextInput(attrs={'class': 'form-input'}),
            'version_number': forms.NumberInput(),
        }

    # def clean_version_status(self):
    #     cleaned_data = self.cleaned_data['is_active']
    #
    #
    #     print(cleaned_data)
    #     return cleaned_data
