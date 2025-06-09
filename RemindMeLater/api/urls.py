from django.urls import path
from .views import get_reminders, create_reminder, reminder_detail

urlpatterns = [
    path('Reminders/', get_reminders, name='get_reminders'),
    path('Reminders/create/', create_reminder, name='create_reminder'),
    path('Reminders/<int:pk>', reminder_detail, name='reminder_detail')
]
