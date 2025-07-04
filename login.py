import json
from pathlib import Path

archivo_usuarios = Path('usuarios.json')
archivo_sesion = Path('sesion.json')

if not archivo_usuarios.exists():
    with open(archivo_usuarios, 'w') as f:
        json.dump({}, f)

def registrar_usuarios():
    """  Registra un nuevo usuario en un archivo Json
    """
    print('\n 📝 - Registro de nuevo usuario')    
    #cargar usuarios actuales
    with open(archivo_usuarios, 'r') as f:
        usuarios = json.load(f)
    
    usuario = input('📛 - Nombre de Usuario: ').strip()
    if usuario in usuarios:
        print(f" ⚠️ - El usuario '{usuario}' ya existe, intenta con otro")
        return
    contrasenia = input('🔑 -  Contraeña: ').strip()
    
    usuarios[usuario] = contrasenia
    
    with open(archivo_usuarios, 'w') as f:
        json.dump(usuarios, f)
    
    print(f" ✅ - Usuario '{usuario}' registrado con exito")


def iniciar_sesion():
    """ verifica que exista un archivo JSON con usuarios, pide usuario y contraseña
    """
    try:
        with open(archivo_usuarios, 'r') as f:
            usuarios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print('⚠️ - No hay usuarios registrados')
        return
    
    usuario = input('👤 - Nombre de Usuario: ').strip()
    clave = input('🔑 - Contraseña: ').strip()
    
    if usuario in usuarios and usuarios[usuario]== clave:
        print(f"✅ - Binvenido, {usuario}")
        # 🔐 Guardar sesión
        with open(archivo_sesion, 'w') as f:
            json.dump({'usuario': usuario}, f)
            
    else:
        print('❌ - Usuario o contraseña incorrecto')


def cambiar_contrasenia():
    try:
        with open(archivo_usuarios, 'r') as f:
            usuarios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print('❌ -  No hay usuarios registrados')
        return
    
    usuario = input('Nombre de usuario: ').strip()
    clave_actual = input('Contraseña actual: ').strip()
    
    if usuario in usuarios and usuarios[usuarios]== clave_actual:
        nueva_clave = input('Nueva contraseña: ').strip()
        confirmar = input('Confirmar nueva contraseña: ').strip()
        
        if nueva_clave != confirmar:
            print('❌ - La contraseña no coinside')
            return
        
        usuarios[usuario] = nueva_clave
        
        with open(archivo_usuarios, 'w') as f:
            json.dump(usuarios, f, indent=4)
        print('✅ -  Contraseña Cambiada')
    
    else:
        print('❌ - Usuario o contraseña incorrecto')


def obtener_usuario_logueado():
    """Esta función verifica si hay un usuario actualmente logueado.
    """
    if archivo_sesion.exists():
        with open(archivo_sesion, 'r') as f:
            sesion = json.load(f)
            return sesion.get('usuario')
    return None


def cerrar_sesion():
    """Esta función elimina la sesión actual.
    """
    if archivo_sesion.exists():
        archivo_sesion.unlink()


def eliminar_cuenta():
    usuario_actual = obtener_usuario_logueado()
    if not usuario_actual:
        print('No hay usuario logueado')
        return
    print(f"⚠️ - Vas a eliminar tu cuenta: {usuario_actual}")
    contrasenia = input('⚠️ - Confirma tu contraseña: ')
    
    with open(archivo_usuarios, 'r') as f:
        usuarios = json.load(f)
    if usuario_actual in usuarios and usuarios[usuario_actual] == contrasenia:
        del usuarios[usuario_actual]
        with open(archivo_usuarios, 'w') as f:
            json.dump(usuarios, f , indent=4)
        cerrar_sesion()
        print('✅ - Tu cuenta fue eliminada')
    else:
        print('❌ - Contraseña incorrecta, no se elimino')
    

def mostrar_menu():
    print('\n 🧑‍💻 - Bienvenidos al sistema - ')
    print(' 1️⃣. Registrarse')
    print(' 2️⃣. Iniciar Seción')
    print(' 3️⃣. Eliminar cuenta')
    print(' 4️⃣. Salir')

def main():
    while True:
        print("##################################")
        mostrar_menu()
        opcion = input('👉 - Elige una opcion: ')
        if opcion == '1':
            print("##################################")
            registrar_usuarios()
        elif opcion == '2':
            print("##################################")
            iniciar_sesion()
        elif opcion == '3':
            print("##################################")
            eliminar_cuenta()
        elif opcion == '4':
            print("##################################")
            print('👋 - Hasta Luego')
            break
        else:
            print('❌ Opcion no valida, intente de nuevo')
        
        
if __name__ == '__main__':
    main()