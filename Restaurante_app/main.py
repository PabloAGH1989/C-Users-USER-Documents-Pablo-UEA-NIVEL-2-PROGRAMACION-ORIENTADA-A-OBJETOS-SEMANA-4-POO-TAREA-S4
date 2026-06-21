from modelos.cliente import cliente
from modelos.producto import producto
from servicios.restaurante_service import restaurante_service 

producto1 = producto("Hamburguesa", 5.99)
producto2 = producto("Pizza", 8.99)   
cliente1 = cliente("Juan", "Perez", "123456789", "juan@patito.com")
cliente2 = cliente("Maria", "Gomez", "987654321", "maria@patito.com")
restaurante = restaurante_service()
restaurante.agregar_cliente(cliente1)   
restaurante.agregar_cliente(cliente2)
restaurante.agregar_producto()
print("clientes registrados:")
restaurante.mostrar_clientes()
print("\nProductos disponibles:")
restaurante.mostrar_productos()
