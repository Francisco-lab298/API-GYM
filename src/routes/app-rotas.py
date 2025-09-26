from flask import Flask, request, jsonify
app = Flask(__name__)

#rota home teste
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

    # Verifica se todos os campos obrigatórios foram fornecidos
    if not nome or not email or not senha or not repetir_senha:
        return jsonify({"error": "Nome, email e senha são obrigatórios!"}), 400

    # Verifica se a senha e a repetição da senha são iguais
    if senha != repetir_senha:
        return jsonify({"error": "As senhas não coincidem!"}), 400

    return jsonify({"message": "Usuário registrado com sucesso!"}), 201