from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import send_contact_email

@csrf_exempt
def send_email_view(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST allowed"},
            status=405
        )

    try:
        data = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    name = data.get("name")
    email = data.get("email")
    website = data.get("website")
    message = data.get("message")

    if not name or not email or not message:
        return JsonResponse(
            {"error": "Missing required fields"},
            status=400
        )

    send_contact_email(name, email, message, website)

    return JsonResponse({"success": True})
