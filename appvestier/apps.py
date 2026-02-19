from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AppvestierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appvestier'

    def ready(self):
        # Este código se ejecuta cuando Django inicia
        post_migrate.connect(create_admin_user, sender=self)

def create_admin_user(sender, **kwargs):
    from django.contrib.auth.models import User
    import os
    
    # Solo lo creamos si no existe
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='denixon13',
            email='denixon13@gamil.com',
            password='Deneicis29*'
        )
        print("Superusuario creado con éxito")