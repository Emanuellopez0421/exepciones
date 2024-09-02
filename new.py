x=-1
if x < 0 :
    raise ValueError("El número no puede ser negativo")


class MiExcepcion("Exepcion"):
    pass

raise MiExcepcion ("Este es un mensaje de error personalizado")
