import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # create instance (do NOT save yet)
            result = MyModel(
                name=data.get('name'),
                age=data.get('age'),
                email=data.get('email'),
                phone=data.get('phone'),
                salary=data.get('salary'),
            )

            result.full_clean()
            result.save()

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse({'message': 'successfully added'}, status=201)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
