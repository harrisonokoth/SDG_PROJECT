from django.db import models
from django.utils import timezone


class Mother(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()  # Mother's date of birth
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)  # Record creation date

    # Health Information
    last_checkup_date = models.DateField(default=timezone.now)  # Last health checkup date
    next_checkup_date = models.DateField(null=True, blank=True)  # Scheduled next checkup date
    medical_history = models.TextField(null=True, blank=True)  # Past medical conditions or health issues

    # Address Information
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    # Record keeping
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set when the record is created
    date_updated = models.DateTimeField(auto_now=True)  # Automatically updated when the record is modified

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name="children")
    first_name = models.CharField(max_length=100)  # Child's first name
    last_name = models.CharField(max_length=100)    # Child's last name
    date_of_birth = models.DateField()               # Child's date of birth
    vaccinated = models.BooleanField(default=False)  # Vaccination status
    registration_date = models.DateTimeField(auto_now_add=True)  # Record creation date

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class HealthRecord(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name="health_records")
    checkup_date = models.DateField()                # Date of the health checkup
    weight = models.FloatField()                      # Weight during checkup
    blood_pressure = models.CharField(max_length=20) # Blood pressure reading
    next_checkup_date = models.DateField(null=True, blank=True)  # Scheduled next checkup date

    def __str__(self):
        return f"Record for {self.mother.first_name} {self.mother.last_name} on {self.checkup_date}"
