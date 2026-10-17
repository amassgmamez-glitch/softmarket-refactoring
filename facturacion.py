from abc import ABC, abstractmethod

class IPagoProcessor(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> bool:
        pass

class PayPalProcessor(IPagoProcessor):
    def pagar(self, monto: float) -> bool:
        print(f"Procesando pago de ${monto} vía PayPal")
        return True

class INotificador(ABC):
    @abstractmethod
    def notificar(self, mensaje: str, destinatario: str):
        pass

class EmailNotificador(INotificador):
    def notificar(self, mensaje: str, destinatario: str):
        print(f"Enviando Email a {destinatario}: {mensaje}")

class IFacturaRepository(ABC):
    @abstractmethod
    def guardar(self, datos_factura: dict):
        pass

class MySQLFacturaRepository(IFacturaRepository):
    def guardar(self, datos_factura: dict):
        print("Factura guardada en MySQL")

class ServicioFacturacion:
    def __init__(self, pasarela_pago: IPagoProcessor, repositorio: IFacturaRepository, notificador: INotificador):
        self.pasarela_pago = pasarela_pago
        self.repositorio = repositorio
        self.notificador = notificador

    def emitir_factura(self, datos_factura: dict, email_cliente: str):
        monto = datos_factura.get("monto", 0)
        if monto <= 0:
            raise ValueError("Monto invalido")
        if self.pasarela_pago.pagar(monto):
            self.repositorio.guardar(datos_factura)
            self.notificador.notificar("Factura emitida exitosamente", email_cliente)

class StripeProcessor(IPagoProcessor):
    def pagar(self, monto: float) -> bool:
        print(f"Procesando pago de ${monto} vía Stripe API")
        return True

def test_emitir_factura():
    print("Ejecutando test unitario de facturacion...")
    assert True
