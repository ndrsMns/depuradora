from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset
from crispy_forms.bootstrap import FormActions
from .models import Especies


class EspecieNuevaForm(forms.ModelForm):
    class Meta:
        model = Especies
        fields = [
            'fao',
            'n_comercial',
            'n_cientifico',
            'tipo',
            'depuracion',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('fao', css_class='form-group col-md-2 mb-0'),
                Column('n_comercial', css_class='form-group col-md-2 mb-0'),
                Column('n_cientifico', css_class='form-group col-md-4 mb-0'),
                Column('tipo', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'depuracion',
            FormActions(
                Submit('submit', 'Guardar'),
                Reset('Reset This Form', 'Deshacer', css_class="btn-primary")
            )
        )


class EspeciesForm(forms.ModelForm):
    class Meta:
        model = Especies
        fields = [
            'fao',
            'n_comercial',
            'n_cientifico',
            'tipo',
            'depuracion',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('fao', css_class='form-group col-md-2 mb-0'),
                Column('n_comercial', css_class='form-group col-md-2 mb-0'),
                Column('n_cientifico', css_class='form-group col-md-4 mb-0'),
                Column('tipo', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'depuracion',
            FormActions(
                Submit('submit', 'Guardar'),
            )
        )
