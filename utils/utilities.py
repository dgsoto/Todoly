import base64

def generar_basic_auth_header(username, password):
    # Combina el nombre de usuario y la contraseña en el formato "username:password"
    credentials = f"{username}:{password}"

    # Codifica las credenciales en Base64
    credentials_base64 = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # Construye el encabezado de autenticación básica
    basic_auth_header = f"Basic {credentials_base64}"

    return basic_auth_header

# Ejemplo de uso
username = "dgsotoqatesting@gmail.com"
password = "dgs1987todoly"
header = generar_basic_auth_header(username, password)

print("Encabezado de Autenticación Básica:", header)