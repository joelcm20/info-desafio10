from .models import NAME_COLLABORATOR_GROUP, NAME_REGISTERED_GROUP


def is_collaborator(user):
    collaborator = user.groups.filter(name=NAME_COLLABORATOR_GROUP).exists()
    registered = user.groups.filter(name=NAME_REGISTERED_GROUP).exists()
    return collaborator or collaborator and registered


def is_registered(user):
    registered = user.groups.filter(name=NAME_REGISTERED_GROUP).exists()
    collaborator = user.groups.filter(name=NAME_COLLABORATOR_GROUP).exists()
    return registered or registered and collaborator or collaborator
