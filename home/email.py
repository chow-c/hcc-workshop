from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email():

    subject, from_email, to = (
        "TestTemplate",
        "ANU HCC Workshop <***REMOVED***>",
        "***REMOVED***",
    )

    text_content = "Test2"

    html_content = render_to_string("home/email_test.html")

    email = EmailMultiAlternatives(
        subject, text_content, from_email, [to], reply_to=["***REMOVED***"]
    )
    email.attach_alternative(html_content, "text/html")

    return email.send(fail_silently=False)
