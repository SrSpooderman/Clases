"""
Texto = str
Numerico = int, float, complex
Secuenciales = list, tuple, range
Mapeado = dict
Set = set, frozenset
Booleano = bool
Binario = bytes, bytearray, memoryview
None = NoneType
"""

#Como saber de que tipo es el dato
x = "Hola" #str
x = 20 #int
x = 20.5 #float
x = 1j #complex
x = ["manzana", "platano", "cereza"] #lista
x = ("manzana", "platano", "cereza") #tupla
x = range(6) #rango
x = {"name" : "John", "age" : 36} #dict
x = {"manzana", "platano", "cereza"} #set
x = frozenset({"manzana", "platano", "cereza"}) #frozenset
x = True #bool
x = b"Hello" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview
x = None #NoneType
