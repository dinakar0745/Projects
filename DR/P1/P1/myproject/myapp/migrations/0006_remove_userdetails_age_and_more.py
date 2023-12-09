# Generated by Django 4.2.7 on 2023-11-05 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_medicinereminder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='medicines_prescribed',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='uploaded_date',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='hospital_name',
            field=models.CharField(default='No Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(upload_to='user_images/'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='image_type',
            field=models.CharField(choices=[('Prescription', 'Prescription'), ('Other', 'Other'), ('MRI', 'MRI'), ('CT Scan', 'CT Scan'), ('X-ray', 'X-ray'), ('Mammogram', 'Mammogram'), ('Ultrasound', 'Ultrasound'), ('Fluoroscopy', 'Fluoroscopy'), ('PET Scans', 'PET Scans')], default='Other', max_length=20),
        ),
    ]
