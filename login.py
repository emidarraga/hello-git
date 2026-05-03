user = "admin"
password = 123456789

def validate_login(user, pwd):
    if user == user and pwd == password:
        return "Bienvenido v2"
    
    return "Datos incorrectos"

print(validate_login("assdds",3233))