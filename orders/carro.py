class Carro:
    def __init__(self, request):    
        self.request = request
        self.session = request.session
        carro= self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}

        self.carro = carro
    
    def agregar(self, producto, atributo):
        clave = f"{producto.id}-{atributo.id}"  # clave única por producto + talla

        if clave not in self.carro:
            self.carro[clave] = {
                "producto_id": producto.id,
                "atributo_id": atributo.id,  
                "nombre": producto.nombre,
                "talla": atributo.valor,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url if producto.imagen else ''
            }
        else:
            self.carro[clave]["cantidad"] += 1
            self.carro[clave]["precio"] = str(
                float(self.carro[clave]["precio"]) + float(producto.precio)
            )

        self.guardar_carro()



    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar(self, producto_id, atributo_id):
        clave = f"{producto_id}-{atributo_id}"
        if clave in self.carro:
            del self.carro[clave]
            print("Intentando eliminar:", clave)
            print("Carrito antes:", self.carro)
            self.guardar_carro()
    
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['cantidad'] -= 1
                value['precio'] = str(float(value['precio']) - float(producto.precio))
                if value['cantidad'] <= 0:
                    self.eliminar(producto)
                break
        self.guardar_carro()   

    def limpiar_carro(self):
        self.session['carro'] = {} 
        self.session.modified = True
            
    def __len__(self):
        return sum(item['cantidad'] for item in self.carro.values())
    
    def finalizar_compra(self):
        if not self.request.user.is_authenticated:
            return None

        from orders.models import Pedido, ItemPedido
        from products.models import Producto, AtributoProducto

        pedido = Pedido.objects.create(usuario=self.request.user)

        for clave, datos in self.carro.items():
            producto = Producto.objects.get(id=datos['producto_id'])
            atributo = AtributoProducto.objects.get(id=datos['atributo_id'])
            cantidad = datos['cantidad']
            precio_unitario = producto.precio  # o atributo.precio si varía por talla

            ItemPedido.objects.create(
                pedido=pedido,
                producto=producto,
                atributo=atributo,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )

        self.limpiar_carro()
        return pedido
    