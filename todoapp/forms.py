from dataclasses import fields
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, HTML, Div
from .models import StudentList


class StudentListForm(forms.ModelForm):

    class Meta:
        model = StudentList
        fields = '__all__'
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('name', css_class='col-md-6 mb-1'),
                Column('email', css_class='col-md-6 mb-1'),
                Column('roll_no', css_class='col-md-6 mb-1'),
                Column('address', css_class='col-md-6 mb-1'),
                
                
                
                css_class='row'
            ),
        )    