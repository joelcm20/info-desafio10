from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Usuario


@receiver(post_save, sender=Usuario)
def add_user_to_registered_group(sender, instance, created, **kwargs):
    if created:
        registered_group, _ = Group.objects.get_or_create(name="Registered")
        instance.groups.add(registered_group)
