# usuarios/signals.py o carrito/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from orders.carro import Carro # ajusta el import según tu estructura

@receiver(user_logged_in)
def migrar_carrito_session(sender, request, user, **kwargs):
    Carro(request).finalizar_compra()
    print(f"Carrito migrado para {user.username}")

