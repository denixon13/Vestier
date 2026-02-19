from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AppvestierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appvestier'

    def ready(self):
        # Importamos DENTRO de la función para evitar el error AppRegistryNotReady
        from django.db.models.signals import post_migrate
        
        def create_admin_user(sender, **kwargs):
            from django.contrib.auth.models import User
            import os
            
            username = os.environ.get('ADMIN_USERNAME', 'denixon13')
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email='denixon13@gmail.com',
                    password=os.environ.get('ADMIN_PASSWORD', 'Deneicis29*')
                )

        post_migrate.connect(create_admin_user, sender=self)