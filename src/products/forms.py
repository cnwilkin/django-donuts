from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "BAM Title"})
    )
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Show me the loot",
                "class": "new-class-name two",
                "rows": 20,
                "cols": 60,
            }
        ),
    )
    price = forms.DecimalField(initial=10000)

    class Meta:
        model = Product
        fields = ["title", "description", "price"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid emaiil")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "BAM Title"})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Show me the loot",
                "class": "new-class-name two",
                "rows": 20,
                "cols": 60,
            }
        ),
    )
    price = forms.DecimalField(initial=10000)
