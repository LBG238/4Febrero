class Jose:
    def __init__(self):
        self.nombre= "Jose Luis"
    def decir_nombre(self):
        nombre = self.nombre
        print(f"Me llamo {nombre}")

persona = Jose()
print(persona.nombre)
persona.decir_nombre()