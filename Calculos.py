#Función con parámetros y con retorno
def es_surfeable(altura):
    return altura >= 1.5

#Función con parámetros y sin retorno
def alertar_vientos_peligroso(nudos_viento):
    if nudos_viento > 20:
        print("\n[ALERTA CRITICA] Viento peligroso, peligro de corriente")
    else:
        print("\nCondiciones de viento dentro del limite")
   
#Función sin parámetros y con retorno
def obtener_temperatura_limite_traje():
    temperatura_limite = 13
    return temperatura_limite

#Función sin parámetros y sin retorno
def mostrar_advertencia_marejada():
    print("\n-------------------------------------")
    print("AVISO DE LA ARMADA: MAREJADAS ACTIVAS")
    print("-------------------------------------")