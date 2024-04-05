class Persona:
    def __init__(self, nombre, correo, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.mensaje = mensaje

    def formato_doc(self):
        return {
            'nombre': self.nombre,
            'correo': self.correo,
            'mensaje': self.mensaje
        }