from django import forms
from catalog.models import Product


FORBIDDEN_WORDS = 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар'


class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in FORBIDDEN_WORDS.replace(', ', ' ').split():
            if word.lower() in cleaned_data.lower().split():
                raise forms.ValidationError('Обнаружены недопустимые слова в описании')

        return cleaned_data
