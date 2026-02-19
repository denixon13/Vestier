from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
import os

class AppvestierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appvestier'

    def ready(self):
        # Este código se ejecuta cuando Django inicia
        post_migrate.connect(create_admin_user, sender=self)

def create_admin_user(sender, **kwargs):
    
    username = 'denixon13' # El usuario que te dio el error
    
    # Usamos get_or_create para que si existe, no haga nada
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email='admin@ejemplo.com',
            password='TuPasswordSeguro123'
        )
        print(f"Superusuario {username} creado con éxito")
    else:
        print(f"El usuario {username} ya existe, saltando creación.")