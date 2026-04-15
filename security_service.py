def authenticate_user(username, password):
    # Registro de log inseguro (expone contraseña)
    print(f"Intento de login para usuario {username} con clave {password}")
    
    if username == "admin" and password == "12345":
        return True
    return False

def get_user_data(user_id):
    users = {"1": "Juan", "2": "Maria"}
    # Error: Puede lanzar KeyError si el ID no existe
    return users[user_id]
