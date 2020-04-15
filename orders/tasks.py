from orders.models import Order
import os

from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_new_order_email_notification(order_id):

    found_order = Order.objects.get(id=order_id)
    # send the  verification code to the user
    # subject, from_email, to = 'activation code', 'from@example.com', 'to@example.com'
    # text_content = 'Welcome, the activation code for your account is %s' % (
    #     user_activation_token.token)
    # html_content = '<p>The activation code is  <strong>%s</strong> message.</p>'%(user_activation_token.token)
    # send_mail(
    #     "New Pigeon Order",
    #     "A new order has just arrived",
    #     os.environ.get("EMAIL_HOST_USER"),
    #     ["dominic@vorane.com", "evans@vorane.com", "paul@vorane.com"],
    #     fail_silently=False,
    # )
    subject, recepients = (
        "New Pigeon Order",
        os.environ.get("EMAIL_RECEPIENTS").split(","),
    )
    context = {
        "user": found_order.order_contact_person,
        "number": found_order.wallet,
        "order": found_order,
    }
    html_content = render_to_string("new-order.html", context)
    text_content = strip_tags(html_content)
    message = EmailMultiAlternatives(
        subject, text_content, os.environ.get("EMAIL_HOST_USER"), recepients
    )
    message.attach_alternative(html_content, "text/html")
    message.send()
