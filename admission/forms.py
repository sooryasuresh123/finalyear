from django import forms
from .models import Department,Program,Student,TransferCertificate, Caste, Religion, Quota,ProgramLevel,Scholarship, StudentScholarship,QualifiedMark,Category,User


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name']
        widgets = {
            'dept_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department name'}),
        }
class ProgramForm(forms.ModelForm):
    class Meta:
        model =Program
        fields = '__all__'
        program_level= forms.ModelChoiceField(queryset=ProgramLevel.objects.all(), required=False)
        department= forms.ModelChoiceField(queryset=Department.objects.all(), required=False)
        widgets = {
            'program_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter program name'}),

        }
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Includes all fields from the model
        exclude = ['user']
        stud_reg_no = forms.CharField(required=False)  # ✅ Optional
        stud_adm_no = forms.CharField(required=False)  # ✅ Optional
        stud_roll_no = forms.CharField(required=False)  # ✅ 
        
        caste = forms.ModelChoiceField(queryset=Caste.objects.all(), required=False)
        religion = forms.ModelChoiceField(queryset=Religion.objects.all(), required=False)
        quota = forms.ModelChoiceField(queryset=Quota.objects.all(), required=False)
        # category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'egrantz': forms.CheckboxInput(),
            'status': forms.CheckboxInput(),
            
        }

    def clean_aadhaar(self):
        aadhaar = self.cleaned_data.get("aadhaar")
        if len(aadhaar) != 12 or not aadhaar.isdigit():
            raise forms.ValidationError("Aadhaar number must be 12 digits.")
        return aadhaar

    def clean_pincode(self):
        pincode = self.cleaned_data.get("pincode")
        if len(pincode) != 6 or not pincode.isdigit():
            raise forms.ValidationError("Pincode must be 6 digits.")
        return pincode
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if not photo.name.lower().endswith(('jpg', 'jpeg', 'png')):
                raise forms.ValidationError("Only JPG, JPEG, and PNG files are allowed.")
        return photo
    def save(self, commit=True):
        # Save the user instance
        student = super().save(commit=False)
        
        if student.pk:
            if student.user_id:
                student.user_id.delete()
        
        # Create the corresponding user
        user = User.objects.create_user(
            username=self.cleaned_data['stud_name'],  # Use email as username
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],  # Set the password
        )
        student.user_id = user  # Link the teacher to the user
        
        if commit:
            student.save()
        
        return student

class TransferCertificateForm(forms.ModelForm):
    class Meta:
        model = TransferCertificate
        fields = ['tc_no', 'stud', 'date_of_application', 'date_of_issue', 'reason']
        widgets = {
            'date_of_application': forms.DateInput(attrs={'type': 'date'}),
            'date_of_issue': forms.DateInput(attrs={'type': 'date'}),
        }

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = '__all__' 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Scholarship Name'}),
        }

class StudentScholarshipForm(forms.ModelForm):
    class Meta:
        model = StudentScholarship
        fields = ['student', 'scholarship', 'amount']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'scholarship': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
        }
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['user_id', 'password', 'role']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }


# class UserForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         label="Confirm Password"
#     )

#     class Meta:
#         model = User
#         fields = ['user_id', 'password', 'confirm_password', 'role']
#         widgets = {
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             self.add_error('confirm_password', "Passwords do not match!")

#         return cleaned_data
    
class QualifiedMarkForm(forms.ModelForm):
    class Meta:
        model = QualifiedMark
        fields = ['stud', 'board', 'normalized_marks']
    
