from django.db import models

# Create your models here.
class Reminder(models.Model):
    MODE_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    date = models.DateField()
    time = models.TimeField()
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder on {self.date} at {self.time} via {self.mode}"