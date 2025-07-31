from flask import Flask
app = Flask(__name__)#revisar o name / chamando função flask para ser usada

@app.route('/')#criando a rota / definindo o caminho que será acessado
def hello_world():#chamando minha rota parar criar as funções
    return {"Message": "Hello World!"}#o retorno após chamar a rota
if __name__ == '__main__':#verificando se o arquivo está sendo executado diretamente / revisar a função para entender
    app.run(debug=True)






