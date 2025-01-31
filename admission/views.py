from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department,Program,Student
from .forms import DepartmentForm,ProgramForm,StudentForm


def index(request):
    return render(request,"index.html")


def manage_department(request):
    departments = Department.objects.all()
    return render(request, 'manage_department.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_department')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('manage_department')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'edit_department.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('manage_department')
    return render(request, 'delete_department.html', {'department': department})


def manage_program(request):
   programs = Program.objects.all()
   return render(request, 'manage_program.html', {'programs': programs})

def add_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_program')
    else:
        form = ProgramForm()
    return render(request, 'add_program.html', {'form': form})

def edit_program(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('manage_program')
    else:
        form =ProgramForm(instance=program)
    return render(request, 'edit_program.html', {'form': form})

def delete_program(request, pk):
   program = get_object_or_404(Program, pk=pk)
   if request.method == 'POST':
        program.delete()
        return redirect('manage_program')
   return render(request, 'delete_program.html', {'program': program})

def manage_student(request):
    students = Student.objects.all()
    return render(request, 'manage_student.html', {'students': students})
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manage_student")  # Change this to your student listing page
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("manage_student")  # Redirect to student list
    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {"form": form})

def delete_student(request, pk):
   student = get_object_or_404(Student, pk=pk)
   if request.method == 'POST':
        student.delete()
        return redirect('manage_student')
   return render(request, 'delete_student.html', {'student': student})


