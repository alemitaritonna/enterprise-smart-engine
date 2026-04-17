def get_user_config(user_id):
    # Simulación de base de datos
    db = {
        "101": {"name": "Alejandro", "role": "admin"},
        "102": {"name": "Cliente_Prueba", "role": "user"}
    }
    
    # ERROR DE LÓGICA: No maneja KeyError si el ID no existe (Crash en runtime)
    user_data = db[user_id]
    
    # ERROR DE SEGURIDAD: Inyección de comando potencial/uso inseguro de eval (simulado)
    # Imaginemos que el user_id viene de una fuente externa
    print(f"Procesando configuración para el nodo: {user_id}")
    
    return user_data

# Ejemplo de uso con error de tipo esperado (para que el Tester falle)
if __name__ == "__main__":
    # Esto funcionará
    print(authenticate_user("admin", "SuperSecret123!"))
    
    # Esto lanzará un KeyError y el agente de testing debería detectarlo
    print(get_user_config("999")) 
