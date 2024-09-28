from django import forms
from .models import Mother, Child, HealthRecord
from datetime import datetime

class MotherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Mother
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'address', 'city', 'country']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        input_formats = ['%Y-%m-%d', '%d/%m/%Y']  # Accepts both formats

        if isinstance(date_of_birth, str):
            for format in input_formats:
                try:
                    date_of_birth = datetime.strptime(date_of_birth, format).date()
                    break  # Successfully parsed date
                except ValueError:
                    continue
            else:
                raise forms.ValidationError("Enter a valid date.")

        # Check for future dates
        if date_of_birth > datetime.today().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")

        return date_of_birth

class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['mother', 'first_name', 'last_name', 'date_of_birth', 'vaccinated']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        input_formats = ['%Y-%m-%d', '%d/%m/%Y']  # Accepts both formats

        if isinstance(date_of_birth, str):
            for format in input_formats:
                try:
                    date_of_birth = datetime.strptime(date_of_birth, format).date()
                    break  # Successfully parsed date
                except ValueError:
                    continue
            else:
                raise forms.ValidationError("Enter a valid date.")

        # Check for future dates
        if date_of_birth > datetime.today().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")

        return date_of_birth

class MotherForm(forms.ModelForm):
    class Meta:
        model = Mother
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        input_formats = ['%Y-%m-%d', '%d/%m/%Y']  # Accepts both formats

        if isinstance(date_of_birth, str):
            for format in input_formats:
                try:
                    date_of_birth = datetime.strptime(date_of_birth, format).date()
                    break  # Successfully parsed date
                except ValueError:
                    continue
            else:
                raise forms.ValidationError("Enter a valid date.")

        # Check for future dates
        if date_of_birth > datetime.today().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")

        return date_of_birth

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['mother', 'checkup_date', 'weight', 'blood_pressure', 'next_checkup_date']
        widgets = {
            'checkup_date': forms.DateInput(attrs={'type': 'date'}),
            'next_checkup_date': forms.DateInput(attrs={'type': 'date'}),
        }
