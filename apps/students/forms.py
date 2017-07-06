from django.forms import ModelForm
from .models import Student

class CreateStudentForm(ModelForm):
    
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'email',
            'starting_cohort'
        )