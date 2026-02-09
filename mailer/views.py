from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import send_contact_email

@csrf_exempt
def send_email_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            website = data.get('website')
            message = data.get('message')

            if send_contact_email(name, email, message, website):
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Fehler beim Senden'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Nur POST erlaubt'})
