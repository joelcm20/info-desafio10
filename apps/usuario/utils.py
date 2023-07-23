from .models import NAME_COLLABORATOR_GROUP, NAME_REGISTERED_GROUP


def is_collaborator(user):
    return user.groups.filter(name=NAME_COLLABORATOR_GROUP).exists()


def is_registered(user):
    return user.groups.filter(name=NAME_REGISTERED_GROUP).exists()
