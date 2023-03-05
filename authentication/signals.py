from .models import User

def create_initial_admin(sender, **kwargs):
    """
    This signal is used for automatically
    creating superuser whenever db is migrated.
    """
    if not User.objects.exists():
        User.objects.create_superuser(username='admin', email='milankatuwal333@gmail.com',password='Admin@12345')