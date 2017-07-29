from django import forms
from .models import Session
class EmailStudentsInSessionForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':50, 'cols':50}
        )
    )
    password = forms.CharField(
        label="Your Dojo Mail Password",
        widget=forms.PasswordInput
    )
    # fields = ('message', 'password')
    # class Meta:
        # model = Session
    # def __init__(self, *args, **kwargs):
    #     print "being inistanitaed"
    #     super(self, EmailStudentsInSessionForm).__init__(*args, **kwargs)
