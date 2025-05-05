from auth.login import verificar_credenciales

dni = input("DNI: ")
email = input("Email: ")

cliente = verificar_credenciales(dni, email)

if cliente:
    print("✅ Login exitoso")
    print(f"Bienvenido, {cliente[1]} {cliente[2]}")
else:
    print("❌ Credenciales inválidas")
