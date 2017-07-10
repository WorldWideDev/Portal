from django.forms import ModelForm
from django import forms
from ..course_sessions.models import Session
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

class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        print 'being initiated'
        student = kwargs['instance']
        try:
            q = Session.objects.filter(students=student)
        except KeyError:
            q = Session.objects.all()
        super(UpdateStudentForm, self).__init__(*args, **kwargs)
        self.fields['session_history'] = forms.ModelMultipleChoiceField(
            required=False, 
            widget=forms.CheckboxSelectMultiple,
            queryset = q
        )
    # def clean_session_history(self):
    #     print self.instance.session_history.all()
    #     print self.cleaned_data['session_history']
    
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
