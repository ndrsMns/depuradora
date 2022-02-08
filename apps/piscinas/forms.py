from django import forms

from .models import Piscinas, Zonas

class PiscinasForm(forms.ModelForm):
    """Form definition for Piscinas."""

    class Meta:
        """Meta definition for Piscinasform."""

        model = Piscinas
        fields ='__all__'


class ZonasForm(forms.ModelForm):
    """Form definition for Zonas."""

    class Meta:
        """Meta definition for Zonasform."""

        model = Zonas
        fields = '__all__'

