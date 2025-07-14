# mystore_project/cart/forms.py

from django import forms

class CartAddProductForm(forms.Form):
    # Change the quantity field to an IntegerField
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        # Use a NumberInput widget and add the classes the theme expects for styling
        widget=forms.NumberInput(attrs={
            'class': 'form-control bg-secondary text-center',
            'value': '1'
        })
    )
    
    # This hidden field tells our cart logic whether to add to the existing quantity or replace it
    override = forms.BooleanField(
                    required=False,
                    initial=False,
                    widget=forms.HiddenInput
                )