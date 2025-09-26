class Usuario:
    def __init__(self, nome, idade, altura, peso, genero, mc, email):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.mc = mc # Imagino que seja IMC (Índice de Massa Corporal)
        self.email = email
    
    def to_dict(self):
        """Retorna uma representação da classe em formato de dicionário."""
        return {
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura,
            "peso": self.peso,
            "genero": self.genero,
            "mc": self.mc,
            "email": self.email
        }