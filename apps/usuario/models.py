from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.


class Usuario(AbstractUser):
    pass

NAME_COLLABORATOR_GROUP = "Collaborator"
NAME_REGISTERED_GROUP = "Registered"

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    registered_group, _ = Group.objects.get_or_create(name=NAME_REGISTERED_GROUP)
    collaborator_group, _ = Group.objects.get_or_create(name=NAME_COLLABORATOR_GROUP)
