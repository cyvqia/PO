class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def perfil(self):
        print(f"O email inserido é {self.email}.")
        print(f"A senha inserida é {self.senha}")

info1 = Usuario("gvdgvwgdv@gmail.com", "123456789")

info1.perfil()