from django import forms
from .models import ProductsModel


class ProductForm(forms.ModelForm):
    def save(self, commit=True, **kwargs):
        instance = super(ProductForm, self).save(commit=False)
        instance.description = instance.description + "..."
        instance.user = kwargs["user"]
        if commit:
            instance.save()
        return instance

    class Meta:
        model = ProductsModel
        fields = ["tittle", "description"]
    
