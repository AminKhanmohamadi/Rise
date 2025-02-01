from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import Customer

@receiver(post_save, sender=CustomUser)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        fullname = f"{instance.first_name} {instance.last_name}".strip() or instance.email.split('@')[0]  # مقداردهی fullname
        Customer.objects.create(owner=instance, name=fullname)
