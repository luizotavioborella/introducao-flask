from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/ola')
def ola():
    nome = 'Vasco'
    return render_template('index.html', nome=nome)



@app.route('/nomes')
def nomes():
    nomes = ['Gabriel', 'Luiz', 'Vitória', 'Renata Mendes']
    return render_template('nomes.html', lista = nomes)

@app.route('/alunos')
def alunos():
    nomes = ['Borella', 'Vasco', 'Letícia', 'Sofia']
    return render_template('alunos.html', alunos = nomes)

@app.route('/logada')
def logada():
    logado = True
    return render_template('perfil.html', logada = logado)

if __name__ == '__main__':
    app.run(debug=True)