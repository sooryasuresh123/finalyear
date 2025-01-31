from django import forms
from .models import Department,Program,Student

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
        fields = ['program_name']
        widgets = {
            'program_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter program name'}),
        }
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Includes all fields from the model

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

