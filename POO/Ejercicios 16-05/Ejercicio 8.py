from abc import ABC, abstractmethod

def requiere_autorizacion(funcion):
    def envoltura(instancia, *args, **kwargs):

        if not instancia.autorizado:
            print("Error: No tienes autorización para registrar logs.")
            return None
        return funcion(instancia, *args, **kwargs)
    return envoltura

class LoggerBase(ABC):
    @abstractmethod
    def registrar(self, mensajes):
        pass

class LogConsola(LoggerBase):
    def __init__(self, nivel_activo, autorizado=False):

        self.__nivel_activo = nivel_activo 
        self.autorizado = autorizado

    @requiere_autorizacion
    def registrar(self, tuplas_mensajes):
        print("PROCESANDO LOGS")
        for nivel, mensaje in tuplas_mensajes:
            if nivel >= self.__nivel_activo:
                print(f"[Nivel {nivel}] Registrado: {mensaje}")

                

logs_sistema = [
    (1, "Usuario entró al sistema"),
    (2, "Cambio de configuración menor"),
    (4, "Advertencia: Espacio en disco bajo"),
    (5, "CRÍTICO: Equipo comprometido")
]

print("Intento 1: Usuario sin permisos")
logger_denegado = LogConsola(nivel_activo=3, autorizado=False)
logger_denegado.registrar(logs_sistema)

print("\nIntento 2: Usuario con permisos (Nivel activo 3)")
logger_permitido = LogConsola(nivel_activo=3, autorizado=True)
logger_permitido.registrar(logs_sistema)    