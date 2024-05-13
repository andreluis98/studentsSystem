from django import forms
from .models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_number': 'Matricula',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'field_of_study': 'Curso',
            'gpa': 'Media',
        }

        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }
