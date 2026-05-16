from abc import ABC, abstractmethod

def validar_tipo_estado(func):
    def envoltura(self, nuevo_estado):
        if not isinstance(nuevo_estado, bool):
            raise ValueError("Error: El estado del servidor debe ser un booleano (True o False).")
        return func(self, nuevo_estado)
    return envoltura

class IObservador(ABC):
    @abstractmethod
    def actualizar(self, estado: bool):
        pass

class ISujeto(ABC):
    @abstractmethod
    def agregar_observador(self, observador: IObservador):
        pass

    @abstractmethod
    def notificar_observadores(self):
        pass

class AlertaEmail(IObservador):
    def actualizar(self, estado: bool):
        if not estado:
            print("📧 [AlertaEmail]: ¡ALERTA! El servidor se ha caído. Enviando correo al equipo IT...")

class SistemaReinicio(IObservador):
    def actualizar(self, estado: bool):
        if not estado:
            print("🔄 [SistemaReinicio]: Intentando reiniciar el servicio de manera automática...")

class Servidor(ISujeto):
    def _init_(self):
        self.__observadores = []
        self.__estado = True

    def agregar_observador(self, observador: IObservador):
        self.__observadores.append(observador)

    def notificar_observadores(self):
        for observador in self.__observadores:
            observador.actualizar(self.__estado)

    @validar_tipo_estado
    def cambiar_estado(self, nuevo_estado: bool):
        self.__estado = nuevo_estado
        estado_str = "ONLINE " if self.__estado else "OFFLINE "
        print(f"\n[Servidor] El estado actual es: {estado_str}")
        
        if self.__estado is False:
            self.notificar_observadores()

if __name__ == "_main_":
    mi_servidor = Servidor()

    alerta_email = AlertaEmail()
    sistema_reinicio = SistemaReinicio()

    mi_servidor.agregar_observador(alerta_email)
    mi_servidor.agregar_observador(sistema_reinicio)

    mi_servidor.cambiar_estado(True)

    mi_servidor.cambiar_estado(False)