import os
import django

def create_superuser():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
    django.setup()
    
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser created successfully!")
    else:
        print("Superuser already exists!")

if __name__ == "__main__":
    create_superuser()
