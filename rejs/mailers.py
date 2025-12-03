from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

FROM = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@zobaczyc.morze")

def send_simple_mail(subject, to_mail, template_base, context):
	TXT = render_to_string(template_base + ".txt", context)
	try:
		HTML = render_to_string(template_base + ".html", context)
	except Exception:
		HTML = None

	send_mail(
		subject=subject,
		message=TXT,
		from_email=FROM,
		recipient_list=[to_mail],
		fail_silently=False,
		html_message=HTML
	)