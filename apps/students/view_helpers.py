from .models import Student
from .forms import CreateStudentForm

def set_context(filter):
    query = Student.objects.student_filter(filter=filter)
    
    return {
        "students": query,
        "form": CreateStudentForm(),
        "filter": filter
    }

