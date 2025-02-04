from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department,Program,Student,Scholarship,TransferCertificate,StudentScholarship
from .forms import DepartmentForm,ProgramForm,StudentForm,ScholarshipForm, TransferCertificateForm,StudentScholarshipForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


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
    program = get_object_or_404(Program, id=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('manage_program')
    else:
        form =ProgramForm(instance=program)
    return render(request, 'edit_program.html', {'form': form,'program': program})

def delete_program(request, pk):
   program = get_object_or_404(Program,id=pk)
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

def manage_scholarship(request):
   scholarships = Scholarship.objects.all()
   return render(request, 'manage_scholarship.html', {'scholarships': scholarships})

def add_scholarship(request):
    if request.method == 'POST':
        form = ScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_scholarship')
    else:
        form = ScholarshipForm()
    return render(request, 'add_scholarship.html', {'form': form})

def edit_scholarship(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    if request.method == 'POST':
        form = ScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            return redirect('manage_scholarship')
    else:
        form =ScholarshipForm(instance=scholarship)
    return render(request, 'edit_scholarship.html', {'form': form})

def delete_scholarship(request, pk):
   scholarship = get_object_or_404(Scholarship, pk=pk)
   if request.method == 'POST':
        scholarship.delete()
        return redirect('manage_scholarship')
   return render(request, 'delete_scholarship.html', {'scholarship': scholarship})

def add_student_scholarship(request):
    if request.method == 'POST':
        form = StudentScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_scholarship')
    else:
        form = StudentScholarshipForm()
    return render(request, 'add_student_scholarship.html', {'form': form})

# def edit_student_scholarship(request, pk):
#     scholarship = get_object_or_404(Scholarship, pk=pk)
#     if request.method == 'POST':
#         form = StudentScholarshipForm(request.POST, instance=scholarship)
#         if form.is_valid():
#             form.save()
#             return redirect('manage_scholarship')
#     else:
#         form =StudentScholarshipForm(instance=scholarship)
#     return render(request, 'edit_scholarship.html', {'form': form})

# def delete_student_scholarship(request, pk):
#    scholarship = get_object_or_404(Scholarship, pk=pk)
#    if request.method == 'POST':
#         scholarship.delete()
#         return redirect('manage_scholarship')
#    return render(request, 'delete_scholarship.html', {'scholarship': scholarship})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                
                return redirect('index')  # Redirect to home page or dashboard
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'login.html')

def transfer_certificate_list(request):
    tc_list = TransferCertificate.objects.all()
    return render(request, 'transfer_certificate_list.html', {'tc_list': tc_list})

def add_transfer_certificate(request):
    if request.method == 'POST':
        form = TransferCertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer_certificate_list')
    else:
        form = TransferCertificateForm()
    return render(request, 'add_transfer_certificate.html', {'form': form})
def edit_transfer_certificate(request, tc_id):
    tc = get_object_or_404(TransferCertificate, id=tc_id)
    
    if request.method == 'POST':
        form = TransferCertificateForm(request.POST, instance=tc)
        if form.is_valid():
            form.save()
            messages.success(request, "Transfer Certificate updated successfully!")
            return redirect('transfer_certificate_list')  # Redirect to TC list page
    else:
        form = TransferCertificateForm(instance=tc)

    return render(request, 'edit_transfer_certificate.html', {'form': form, 'tc': tc})
def delete_transfer_certificate(request, tc_id):
    tc = get_object_or_404(TransferCertificate, id=tc_id)
    
    if request.method == 'POST':
        tc.delete()
        messages.success(request, "Transfer Certificate deleted successfully!")
        return redirect('transfer_certificate_list')  # Redirect to TC list page
    
    return render(request, 'confirm_delete.html', {'tc': tc})
