class Credencial:
    def __init__(self, servicio: str, password: str):
        self.servicio = servicio
        self.password = password

    def __repr__(self):
        return f"Credencial(servicio={self.servicio!r}, password={'*' * len(self.password)})"


def validar_fortaleza(credencial):
    caracteres = {
        'mayusculas': 0,
        'minusculas': 0,
        'digitos': 0,
        'simbolos': 0,
    }

    for caracter in credencial.password:
        if caracter.isupper():
            caracteres['mayusculas'] += 1
        if caracter.islower():
            caracteres['minusculas'] += 1
        if caracter.isdigit():
            caracteres['digitos'] += 1
        if not caracter.isalnum():
            caracteres['simbolos'] += 1

    cumple_longitud = len(credencial.password) >= 8
    tiene_todos = (
        caracteres['mayusculas'] > 0 and
        caracteres['minusculas'] > 0 and
        caracteres['digitos'] > 0 and
        caracteres['simbolos'] > 0
    )

    return {
        'servicio': credencial.servicio,
        'valida': cumple_longitud and tiene_todos,
        'detalle': caracteres,
        'longitud': len(credencial.password),
    }


if __name__ == '__main__':
    credenciales = [
        Credencial('Correo', 'Segura123!'),
        Credencial('Banco', 'banco2026'),
        Credencial('RedSocial', 'Amor#2026'),
    ]

    for cred in credenciales:
        resultado = validar_fortaleza(cred)
        estado = 'SEGURA' if resultado['valida'] else 'NO segura'
        print(f"{resultado['servicio']}: {estado} - longitud={resultado['longitud']}"
              f" - {resultado['detalle']}")
