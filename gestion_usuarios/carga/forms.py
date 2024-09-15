from django import forms


class CargaMasivaForm(forms.Form):
    archivo_csv = forms.FileField()
