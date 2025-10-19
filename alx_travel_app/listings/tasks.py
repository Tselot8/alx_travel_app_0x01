from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(user_email, booking_id):
    send_mail(
        subject="Booking Payment Successful",
        message=f"Your payment for booking {booking_id} was successful.",
        from_email="no-reply@example.com",
        recipient_list=[user_email]
    )
