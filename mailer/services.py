from django.core.mail import send_mail
from django.conf import settings
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def send_contact_email(name: str, email: str, message: str, website: str = None) -> bool:
    """
    Sends an Frontend form data as an e-mail to the specified e-mail.
    Website is optional.
    """
    try:
        website_text = f"Webseite: {website}" if website else "Webseite: keine angabe"

        send_mail(
            subject=f'ersan-bihorac.de: Nachricht von {name}',
            message=f'Name: {name}, {website_text}, E-Mail-adresse: {email}\n\nNachricht: {message}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print("Error when sending Mail:", e)
        return False
