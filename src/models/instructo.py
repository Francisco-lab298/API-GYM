class Instructo: # Classe para representar um instrutor
    def __init__(self, nome, instrutor_id, email, especialidade, idade, genero):
        self.nome = nome
        self.instrutor_id = instrutor_id
        self.email = email
        self.especialidade = especialidade
        self.idade = idade
        self.genero = genero
    
    def to_dict(self):
        """Retorna uma representação da classe em formato de dicionário."""
        return {
            "nome": self.nome,
            "instrutor_id": self.instrutor_id,
            "email": self.email,
            "especialidade": self.especialidade,
            "idade": self.idade,
            "genero": self.genero
        }