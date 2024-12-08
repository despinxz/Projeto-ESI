from flask import Flask, request, redirect, url_for, render_template
from app_ccp import ccp
from app_professor import professor
from app_aluno import aluno
import conn_bd

app = Flask(__name__)
app.secret_key = 'chave'

# Registro dos blueprints
app.register_blueprint(ccp, url_prefix='/ccp')
app.register_blueprint(professor, url_prefix='/professor')
app.register_blueprint(aluno, url_prefix='/aluno')


@app.route('/feedback/<nusp>')
def feedback(nusp):
    return render_template('feedback.html', nusp=nusp)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        nusp = request.form.get('nusp')
        senha = request.form.get('senha')

        sucesso = conn_bd.verificar_login(tipo, nusp, senha)
        if not sucesso:
            return redirect(url_for('login'))
        else:
            tipo_para_rota = {
                'ccp': 'ccp.index',
                'professor': 'professor.index',
                'aluno': 'aluno.index'
            }
            rota = tipo_para_rota.get(tipo)
            return redirect(url_for(rota, nusp=nusp))  
           
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        dados = {
            'nusp': request.form.get('nusp'),
            'nome': request.form.get('nome'),
            'senha': request.form.get('senha'),
        }

        if tipo == 'aluno':
            dados.update({
                'nusp': request.form.get('nusp'),
                'email': request.form.get('email'),
                'data_nasc': request.form.get('data_nasc'),
                'rg': request.form.get('rg'),
                'local_nasc': request.form.get('local_nasc'),
                'nacionalidade': request.form.get('nacionalidade'),
                'lattes': request.form.get('lattes'),
                'orientador': request.form.get('orientador')
            })
        elif tipo == 'professor':
            dados['nusp'] = request.form.get('nusp')

        sucesso = conn_bd.cadastrar_usuario(tipo, dados)
        if sucesso == False:
            return redirect(url_for('cadastro'))
        else:
            return redirect(url_for('login'))           

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)