from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IGORKEVEN'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if nome == 'faustinho' and senha == '123':
            return redirect('/index')  # Redireciona para a rota /index após login bem-sucedido
        else:
            return render_template('login.html', error="Usuário ou senha incorretos")  # Renderiza a página de login com erro em caso de falha
    else:
        return render_template('login.html')  # Renderiza a página de login quando o método é GET

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/matricula')
def matricula():
    return render_template('matricula.html')

@app.route('/lista')
def lista():
    return render_template('lista.html')

if __name__ == "__main__":
    app.run(debug=True)
