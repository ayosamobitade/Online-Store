from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,2)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES, coerce = int)

    override = forms.TypedChoiceField(choices =False, initial = False, widget = forms.HiddenInput)

    
