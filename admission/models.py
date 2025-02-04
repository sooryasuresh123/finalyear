from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.dept_name
class ProgramLevel(models.Model):
    level_name = models.CharField(max_length=100,default='UG')

    def __str__(self):
        return self.level_name

class Program(models.Model):
    program_name = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)  # ForeignKey to Department
    program_level = models.ForeignKey(ProgramLevel, on_delete=models.SET_NULL, blank=True, null=True)  # ForeignKey to ProgramLevel

    def __str__(self):
        return self.program_name
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True,default='Null')

    def __str__(self):
        return self.category_name
class Caste(models.Model):
    caste_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.caste_name


class Religion(models.Model):
    religion_name = models.CharField(max_length=50)

    def __str__(self):
        return self.religion_name


class Quota(models.Model):
    quota_name = models.CharField(max_length=50)

    def __str__(self):
        return self.quota_name



class Student(models.Model):
    stud_name = models.CharField(max_length=100)
    stud_adm_no = models.CharField(max_length=20, unique=True)
    stud_reg_no = models.CharField(max_length=20, unique=True, blank=True, null=True) 
    stud_roll_no = models.CharField(max_length=20, unique=True, blank=True, null=True)
    aadhaar = models.CharField(max_length=12, unique=True)
    abc_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    caste = models.ForeignKey(Caste, on_delete=models.SET_NULL, blank=True, null=True)  # Foreign Key to Caste
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, blank=True, null=True)  # Foreign Key to Religion
    quota = models.ForeignKey(Quota, on_delete=models.SET_NULL, blank=True, null=True)  
    program= models.ForeignKey(Program, on_delete=models.SET_NULL, blank=True, null=True)  # Foreign Key to Quota# Foreign Key to Quota
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
    language=models.CharField(max_length=10, choices=[('Malayalam', 'Malayalam'), ('Hindi', 'Hindi')] ,default='Malayalam')
    identification_mark = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.stud_name} ({self.stud_adm_no})"



class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.scholarship_name
    
class Reason(models.Model):
    reason_description = models.CharField(max_length=255)

    def __str__(self):
        return self.reason_description

class TransferCertificate(models.Model):
    tc_no = models.CharField(max_length=50, unique=True)
    stud = models.ForeignKey('admission.Student', on_delete=models.CASCADE)  # Assuming 'student' is your app name
    date_of_application = models.DateField()
    date_of_issue = models.DateField(null=True, blank=True)
    reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"TC {self.tc_no} - {self.stud}"
