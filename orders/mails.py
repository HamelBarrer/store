from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


class Mail:
    @staticmethod
    def send_complete_order(orden, user):
        subject = 'Tu pedido ha sido enviado'
        template = get_template('order/mails/complete.html')
        content = template.render({
            'user': user,
            'orden': orden,
        })
        message = EmailMultiAlternatives(subject, 'Mensaje importante', settings.EMAIL_HOST_USER, [user.email])
        message.attach_alternative(content, 'text/html')
        message.send()
