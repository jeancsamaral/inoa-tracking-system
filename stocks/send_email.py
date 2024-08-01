import os
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection


def send_email(subject,
               message,
               recipient_list):

    from_email="MS_YBp2om@trial-neqvygm7ykjg0p7w.mlsender.net"
    # Define a lista de destinatários padrão se não for fornecida
    if recipient_list is None:
        recipient_list = ["jeancarlosimpliamaral@hotmail.com"]

    print(recipient_list)
    with get_connection(
        host=settings.MAILERSEND_SMTP_HOST,
        port=settings.MAILERSEND_SMTP_PORT,
        username=settings.MAILERSEND_SMTP_USERNAME,
        password="73CxsRReQLCk1UxC",
        use_tls=True,
    ) as connection:
        email = EmailMessage(
            subject=subject,
            body=message,
            to=recipient_list,
            from_email=from_email,
            connection=connection,
        )
        email.content_subtype = "html"  # Defina o conteúdo do email como HTML
        email.send()
    return JsonResponse({"status": "ok"})



