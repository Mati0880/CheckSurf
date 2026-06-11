from Calculos import es_surfeable,alertar_vientos_peligroso,obtener_temperatura_limite_traje,mostrar_advertencia_marejada
from Pantalla import mostrar_titulo,titulo_menu

def menu():
    mostrar_titulo()
    altura_ola = float(input("Ingrese la altura de las olas en metros: "))
    viento = int(input("Ingrese la velocidad del viento en nudos: "))
    while True:
        titulo_menu()
        print(f"Ola Ingresada: {altura_ola} metros | Viento: {viento} nudos")
        print("[1] ¿Es surfeable hoy?")
        print("[2] Evaluar peligro de viento")
        print("[3] Consultar límite de temperatura")
        print("[4] Ver aviso de la armada")
        print("[5] Actualizar datos")
        print("[6] Salir") 
        opcion = int(input("Seleccione una opción : "))
        if opcion == 1:
            apto = es_surfeable(altura_ola)
            if apto:
                print("\nExcelentes olas para el surf")
            else:
                print("\nEl mar esta muy tranquilo")
        elif opcion == 2:
            alertar_vientos_peligroso(viento)
        elif opcion == 3:
            temperatura_critica = obtener_temperatura_limite_traje()
            print(f"\nRecuerda: bajo los {temperatura_critica}°C es obligatorio usar traje 4/3mm")
        elif opcion == 4:
            mostrar_advertencia_marejada()
        elif opcion == 5:
            altura_ola = float(input("\nIngresa la nueva altura de olas en metros : "))
            viento = int(input("Ingresa la nueva velocidad del viento : "))
            print("[INFO] Datos actualizados")
        elif opcion == 6:
            print("\nsaliendo del sistema .......")
            break
        else:
            print("\nOpcion no válida")
if __name__ == "__main__":
    menu()