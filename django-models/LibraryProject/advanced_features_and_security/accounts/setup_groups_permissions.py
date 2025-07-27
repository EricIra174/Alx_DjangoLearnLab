from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser

# Get the content type for CustomUser model
content_type = ContentType.objects.get_for_model(CustomUser)

# Permissions to assign
permissions = {
    "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
    "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
    "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
    "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
}

# Create groups
groups = {
    "Viewers": ["can_view"],
    "Editors": ["can_view", "can_create", "can_edit"],
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
}

for group_name, perms in groups.items():
    group, created = Group.objects.get_or_create(name=group_name)
    group.permissions.clear()  # Optional: reset if already existed
    for perm_codename in perms:
        group.permissions.add(permissions[perm_codename])

print("Groups and permissions successfully set up!")
