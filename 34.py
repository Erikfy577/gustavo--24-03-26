#Acesso ao Sistema: Peça login e senha. Só aprove se for "admin" e "1234".
login = input("Login: ")
senha = input("Senha: ")
if login == "admin" and senha == "1234":
    print("Acesso concedido. Bem-vindo!")
else:
    print("Login ou senha incorretos.")