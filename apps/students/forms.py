from django.forms import ModelForm
from django import forms
from .models import Student, Alias, Note

class CreateStudentForm(ModelForm):

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'email',
            'starting_cohort'
        )

class CreateAliasForm(ModelForm):
    class Meta:
        model = Alias
        fields = ('source', 'handle')

class CreateNoteForm(ModelForm):
    content = forms.CharField(
        min_length=5, 
        label = "Leave a Note"
    )
    class Meta:
        model = Note
        fields = ('content',)