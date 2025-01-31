from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.dept_name
    
class Program(models.Model):
    program_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.program_name


class Student(models.Model):
    stud_name = models.CharField(max_length=100)
    stud_adm_no = models.CharField(max_length=20, unique=True)
    aadhaar = models.CharField(max_length=12, unique=True)
    abc_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    parent_name = models.CharField(max_length=100)
    parent_mob = models.CharField(max_length=15)
    house_name = models.CharField(max_length=100)
    post = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    date_of_joining = models.DateField()
    income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    egrantz = models.BooleanField(default=False)
    status = models.BooleanField(default=True)  # Active/Inactive
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    blood_group = models.CharField(max_length=5, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B-'), ('O+', 'O-'), ('AB+', 'AB-')])
    identification_mark = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.stud_name} ({self.stud_adm_no})"



