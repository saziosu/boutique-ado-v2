from django import forms
from .models import Product, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # short hand for loop to set the categories in a list
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Update the category names to the friendly names instead of the ID or name field
        self.fields['category'].choices = friendly_names
        # iterate through the rest of the fields
        for field_name, field in self.fields.items():
            # attach some styling to match our store's theme
            field.widget.attrs['class'] = 'border-black rounded-0'