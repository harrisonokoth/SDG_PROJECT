# health/admin.py

from django.contrib import admin
from .models import Mother, Child, HealthRecord

admin.site.register(Mother)
admin.site.register(Child)
admin.site.register(HealthRecord)
