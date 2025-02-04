from django import forms
from .models import Department,Program,Student,Scholarship,TransferCertificate, Caste, Religion, Quota,ProgramLevel,StudentScholarship


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
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Includes all fields from the model
        stud_reg_no = forms.CharField(required=False)  # ✅ Optional
        stud_adm_no = forms.CharField(required=False)  # ✅ Optional
        stud_roll_no = forms.CharField(required=False)  # ✅ 
        
        caste = forms.ModelChoiceField(queryset=Caste.objects.all(), required=False)
        religion = forms.ModelChoiceField(queryset=Religion.objects.all(), required=False)
        quota = forms.ModelChoiceField(queryset=Quota.objects.all(), required=False)

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

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model =Scholarship
        fields = ['scholarship_name']
        widgets = {
            'scholarship_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter scholarship name'}),
        }
class StudentScholarshipForm(forms.ModelForm):
    class Meta:
        model = StudentScholarship
        fields = ['student', 'scholarship', 'amount']

class TransferCertificateForm(forms.ModelForm):
    class Meta:
        model = TransferCertificate
        fields = ['tc_no', 'stud', 'date_of_application', 'date_of_issue', 'reason']
        widgets = {
            'date_of_application': forms.DateInput(attrs={'type': 'date'}),
            'date_of_issue': forms.DateInput(attrs={'type': 'date'}),
        }


