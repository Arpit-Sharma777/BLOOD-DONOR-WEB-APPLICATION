from django.db import models

BLOOD_GROUPS = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    email = models.EmailField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class BloodRequest(models.Model):
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blood_group} in {self.location}"