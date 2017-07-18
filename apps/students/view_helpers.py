from django.core.cache import cache
from .models import Student
from .forms import CreateStudentForm

STUDENTS_CACHE_KEY = "all_students"

def set_context(filter):

    query = cache.get(STUDENTS_CACHE_KEY)
    if not query:
        query = update_student_cache()

    # Previously had left filtering to the ORM
    # With caching run a Server-side filter instead
    # query = Student.objects.student_filter(filter=filter)
    if filter != 'all':
        choice = [item[1] for item in Student.STATUS_CHOICES if item[0] == filter]
        query = [S for S in query if S.status == choice]
    # Can Potentially Cache the Filtered results as well
    
    return {
        "students": query,
        "form": CreateStudentForm(),
        "filter": filter
    }

def update_student_cache():
    students = Student.objects.all()
    cache.set(STUDENTS_CACHE_KEY, students)
    return students