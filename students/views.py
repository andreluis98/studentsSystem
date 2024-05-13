from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Students
from .forms import StudentsForm
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Students.objects.all()
    })


def view_students(request, id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('students:index'))


def add_students(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Students.objects.create(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa
            )
            return render(request, 'students/add.html', {
                'form': StudentsForm(),
                'success': True
            })
    else:
        form = StudentsForm()
    return render(request, 'students/add.html', {
        'form': form,
    })


def edit(request, id):
    student = get_object_or_404(Students, pk=id)

    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentsForm(instance=student)

    return render(request, 'students/edit.html', {
        'form': form
    })


def delete(request, id):
    student = get_object_or_404(Students, pk=id)
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect(reverse('index'))
