# Diccionario global para usuarios
usuarios = {}

# Verificar que no se repita el nombre de usuario
def validar_nombre(usuarios, nombre):
    # while True:            
        for nombre, detail in usuarios.items():
                if nombre in detail["nombre"]:
                    print(f"El nombre del usuario ya existe.")
                    print("Ingrese nuevamente.")
                    continue
                    
                else:
                    print("Nombre ingresado con éxito!")
                    return detail

        if not nombre:
            return None
        return nombre.lower()

def validar_sexo():
    while True:
        sexo = input("Ingrese sexo: ")
        Mf = "MF"

        for genero in str(sexo.upper()):
            if genero in Mf:
                return sexo
            else:
                print("Debe ingresar M o F solamente. Intente de nuevo.")
                continue

#Verificar contraseña segura
def contar_caracteres(contrasena):
    return len(contrasena)
        
def contar_numeros(contrasena):
    contador = 0
    for c in contrasena:
        if c.isnumeric():
            contador += 1
    return contador

def validar_contrasena(contrasena):
    passwd = passwd.strip() #Elimina espacio en blanco al inicio o final del texto
    if " " in passwd: #verifica si contiene espacios en medio
        return None # de ser True devuelve None
    errores = []
    if contar_caracteres(contrasena) < 8:
        errores.append("Mínimo 8 caracteres")
    if contar_numeros(contrasena) < 1:
        errores.append("Al menos 1 número")
    if errores:
        print("Contraseña no válida. Debe contener:")
        for e in errores:
            print(" -", e)
        return False
    return True

def pedir_contrasena_segura():
    while True:
        pwd1 = input("Ingrese contraseña: ")
        # pwd2 = input("Repita la contraseña: ")
        # if pwd1 != pwd2:
        #     print("Las contraseñas no coinciden. Intente nuevamente.")
        #     continue
        # if not validar_contrasena(pwd1):
        #     continue
        return pwd1

def agregar_usuario():
    print("\n--- Agregar nuevo usuario ---")

    nombre = input("Ingrese su nombre de usuario: ").lower()
    nombre_val = validar_nombre(usuarios, nombre)
    sexo = validar_sexo()
    contraseña = pedir_contrasena_segura()

    usuarios[nombre_val] = {
        "nombre": nombre,
        "sexo": sexo,
        "contraseña": contraseña
    }
    print("Usuario ingresado con éxito!!")

def buscar_usuario():
    nombre = input("Ingrese el usuario a buscar: ").strip().lower()
    
    for nombre, detail in usuarios.items():
        if nombre.lower() in detail["nombre"].lower():
            print(f"El sexo del usuario es: {detail['sexo']} y la contraseña es: {detail['contraseña']}")
        else:
            print("Usuario no encontrado.")

def eliminar_usuario():
    nombre = input("Ingrese el usuario a eliminar: ").strip().lower()

    if nombre in usuarios:
        confirm = input(f"¿Seguro que quiere eliminar el usuario {nombre}? (s/n): ").strip().lower()
        if confirm == "s":
            del usuarios[nombre]
            print("Usuario eliminado con éxito!.")
        else:
            print("Eliminación cancelada.")
    else:
        print("El usuario se no encuentra.")

while True:
    print("\n--- MENÚ DE USUARIOS ---")
    print("1) Ingresar usuario")
    print("2) Buscar usuario")
    print("3) Eliminar usuario")
    print("4) Salir")

    try:
        opcion = int(input("Elija opción: "))
        match opcion:
            case 1:
                agregar_usuario()
            case 2:
                buscar_usuario()
            case 3:
                eliminar_usuario()
            case 4:
                print("Programa terminado...")
                break
            case _:
                print("Debe ingresar una opción válida!!")
    except ValueError:
        print("Error. Debe ingresar una opción válida!")
