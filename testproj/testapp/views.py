from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
# Create your views here.


def index(requst):
    return render(requst, 'testapp/index.html')


def addAndShow(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            student_form = StudentForm(label_suffix=' ')

    else:
        student_form = StudentForm(label_suffix=' ')
    all_students = Student.objects.all()
    return render(request, 'testapp/addandshow.html', {'form': student_form, 'all_students': all_students})


def updateStudent(request, id):
    if request.method == 'POST':
        student_obj = Student.objects.get(pk=id)
        student_form = StudentForm(request.POST, instance=student_obj)
        if student_form.is_valid():
            student_form.save()
            return redirect('/')
    else:
        student_obj = Student.objects.get(pk=id)
        student_form = StudentForm(instance=student_obj, label_suffix=' ')
    return render(request, 'testapp/updatestudent.html', {'form': student_form})


def deleteStudent(request, id):
    if request.method == 'POST':
        student_obj = Student.objects.get(pk=id)
        student_obj.delete()
        return redirect('/')
