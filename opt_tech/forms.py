from django import forms

class RowColForm(forms.Form):
    rows = forms.IntegerField()
    cols = forms.IntegerField()
    
    class Meta:
        fields = ('rows','cols')
        widgets = {
            'rows': forms.TextInput(
                attrs={
                    'class': 'form-control',                  
                    'required': 'required',
                    'autofocus': 'autofocus',
                    #'style': 'margin-bottom: 7px;'
                }
            ),
            'cols': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    #'style': 'margin-bottom: 7px;'
                }
            ),
        }