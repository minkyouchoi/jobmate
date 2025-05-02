from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'name', 'phone', 'email',
            'education', 'show_education',
            'experience', 'career_level',
            'preferred_location', 'employment_type',
            'skills', 'skills_detail',
            'bio',
            'portfolio', 'portfolio_link',
        ]
        widgets = {
            'education': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 3}),
            'bio': forms.Textarea(attrs={'rows': 3}),
            'skills_detail': forms.Textarea(attrs={'rows': 3}),
        }
