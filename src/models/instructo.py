class instructo: # Classe para representar um instrutor
    def __init__(self, nome, instrutor_id, email, especialidade, idade, genero):
        self.nome = nome
        self.instrutor_id = instrutor_id
        self.email = email
        self.especialidade = especialidade
        self.idade = idade
        self.genero = genero

    def greet(self):
        return f"Hello, {self.nome, self.instrutor_id, self.email, self.especialidade, self.idade, self.genero}!"