import json
from django.http import JsonResponse
from .models import Task

# Create your views here.
def load_dummy_data(request):
    with open('tasks/dummy_tasks.json', 'r') as file:
        data = json.load(file)
        for task_data in data:
            Task.objects.create(
                title=task_data['title'],
                description=task_data.get('description', ''),
                completed=task_data['completed']
            )
    return JsonResponse({"message": "Dummy tasks loaded successfully"})