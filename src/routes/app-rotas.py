from flask import Flask, request, jsonify
import sys
import os

# Adiciona o diretório raiz do projeto ao path do Python
# Isso permite que o Flask encontre os módulos em 'src/models'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.models.usuario import Usuario

app = Flask(__name__)
usuarios_db = [] # "Banco de dados" em memória para armazenar usuários

#rota home
@app.route('/', methods=['GET'])#definindo o metodo que ira ser usado
def home():
    return jsonify({"message": "Bem-vindo a API de Gerenciamento de Academia!"})

#rota post login
@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    if not dados:
        return jsonify({"error": "Requisição inválida, corpo JSON ausente."}), 400

    email = dados.get('email')
    senha = dados.get('senha')

    if not email or not senha:
        return jsonify({"error": "Email e senha são obrigatórios!"}), 400

    return jsonify({"message": "Login realizado com sucesso!"}), 201

#rota post registro
@app.route('/registro', methods=['POST'])
def registro():
    dados = request.get_json()
    if not dados:
        return jsonify({"error": "Requisição inválida, corpo JSON ausente."}), 400

    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    repetir_senha = dados.get('repetir_senha')

    # Validação de campos básicos
    campos_obrigatorios = ['nome', 'email', 'senha', 'repetir_senha', 'idade', 'altura', 'peso', 'genero']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"error": f"O campo '{campo}' é obrigatório."}), 400

    # Verifica se a senha e a repetição da senha são iguais
    if senha != repetir_senha:
        return jsonify({"error": "As senhas não coincidem!"}), 400
    
    # Verifica se o email já está em uso
    for u in usuarios_db:
        if u.email == email:
            return jsonify({"error": "Este email já está cadastrado."}), 409 # 409 Conflict

    # Cria uma nova instância do usuário (sem salvar a senha em texto plano por enquanto)
    # Em um projeto real, a senha seria criptografada (hashed) aqui.
    novo_usuario = Usuario(
        nome=nome,
        idade=dados.get('idade'),
        altura=dados.get('altura'),
        peso=dados.get('peso'),
        genero=dados.get('genero'),
        mc=dados.get('mc'), # O ideal seria calcular o IMC aqui
        email=email
    )

    # Adiciona o novo usuário ao nosso "banco de dados"
    usuarios_db.append(novo_usuario)

    return jsonify({"message": "Usuário registrado com sucesso!", "usuario": novo_usuario.to_dict()}), 201

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    """Retorna a lista de todos os usuários cadastrados."""
    return jsonify([usuario.to_dict() for usuario in usuarios_db])