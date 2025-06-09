from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializer import ReminderSerializer

@api_view(['GET'])
def get_reminders(request):
    Reminders = Reminder.objects.all()
    serializer = ReminderSerializer(Reminders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reminder_detail(request, pk):
    try:
        reminder = Reminder.objects.get(pk=pk)
    except Reminder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)