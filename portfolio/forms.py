from django import forms
from .models import Experience, Education

class ExperienceForm(forms.ModelForm):
    start_date = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM'}))
    end_date = forms.CharField(max_length=7, required=False, widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM'}))

    class Meta:
        model = Experience
        fields = ['job_title', 'company_name', 'start_date', 'end_date', 'description']

class EducationForm(forms.ModelForm):
    start_date = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM'}))
    end_date = forms.CharField(max_length=7, required=False, widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM'}))

    class Meta:
        model = Education
        fields = ['degree', 'school', 'start_date', 'end_date', 'description']
