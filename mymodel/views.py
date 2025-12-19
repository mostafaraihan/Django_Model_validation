import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        MyModel.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email'),
            phone=data.get('phone'),
            salary=data.get('salary'),
        )

        return JsonResponse({'message': 'successfully added'}, status=201)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
