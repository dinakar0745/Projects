from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Model for User Details
class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    hospital_name = models.CharField(max_length=100, default='No Name')
    hospital_address = models.TextField(default='No Address')
    doctor_name = models.CharField(max_length=100, default='No Name')
    disease = models.CharField(max_length=100, default='No Disease')
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image_type = models.CharField(
        max_length=20,
        choices=[

            ('Prescription', 'Prescription'),
            ('Other', 'Other'),
            ('MRI', 'MRI'),
            ('CT Scan', 'CT Scan'),
            ('X-ray', 'X-ray'),
            ('Mammogram', 'Mammogram'),
            ('Ultrasound', 'Ultrasound'),
            ('Fluoroscopy', 'Fluoroscopy'),
            ('PET Scans', 'PET Scans'),

        ],
        default='Other'

    )
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return self.name

# Model for Medicine Reminder
from django.db import models

class MedicineReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    medicine_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    reminder_datetime = models.DateTimeField()
