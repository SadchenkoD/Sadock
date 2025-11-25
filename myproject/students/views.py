from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import UserFormFields, UserFormData
from .models import Student



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def static_files(request):
    return render(request, 'static_files.html')

# Оставь старые функции
def student_detail(request, student_id):
    return HttpResponse(f"<h2>Студент ID: {student_id}</h2>")

def search_student(request):
    name = request.GET.get('name', 'не указано')
    return HttpResponse(f"<h2>Поиск:</h2><p>Имя: <strong>{name}</strong></p>")

def form_html(request):
    return render(request, 'form_html.html')

def form_html_result(request):
    data = {
        'last_name': request.GET.get('last_name'),
        'first_name': request.GET.get('first_name'),
        'middle_name': request.GET.get('middle_name'),
        'age': request.GET.get('age'),
        'address': request.GET.get('address'),
        'group': request.GET.get('group'),
        'subjects': ', '.join(request.GET.getlist('subjects')),
    }
    return render(request, 'form_html_result.html', data)


def students_list(request):
    context = {
        'all_students': Student.objects.all(),
        'student_by_name': Student.objects.filter(last_name="Иванов").first(),
        'students_2000': Student.objects.filter(birth_year=2000),
        'not_group_101': Student.objects.exclude(group_number="101"),
        'first_two': Student.objects.all()[:2],
        'sorted_desc': Student.objects.all().order_by('-last_name'),
    }
    return render(request, 'students_list.html', context)


def fields(request):
    form = UserFormFields(request.GET or None)
    return render(request, 'fields.html', {'form': form})


def userdata(request):
    if request.method == 'POST':
        form = UserFormData(request.POST)
        if form.is_valid():
            student = form.save()
            return render(request, 'userdata.html', {
                'form': UserFormData(),
                'success': f"{student.last_name} {student.first_name}"
            })
    else:
        form = UserFormData()
    return render(request, 'userdata.html', {'form': form})