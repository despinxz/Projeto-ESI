from flask import Flask, request, jsonify, render_template, redirect, url_for
import conn_bd
import psycopg2 
import jwt
from functools import wraps

app = Flask(__name__)
app.secret_key = 'chave'

@app.route('/<nusp_aluno>')
def index(nusp_aluno):
    return render_template('index_aluno.html', nusp_aluno=nusp_aluno)

@app.route('/tabela_relatorios/<nusp_aluno>')
def tabela_relatorios(nusp_aluno):
    return render_template('tabela_relatorios_aluno.html', nusp_aluno=nusp_aluno)

@app.route('/relatorio/<id>')
def detalhes_relatorio(id):
    return render_template('detalhes_relatorio_aluno.html', relatorio_id=id)

@app.route('/formulario/<nusp_aluno>')
def render_forms_relatorio(nusp_aluno):
    return render_template('formulario_relatorio_aluno.html', nusp_aluno=nusp_aluno)

@app.route('/relatorios/<nusp_aluno>', methods=['GET'])
def get_relatorios_aluno(nusp_aluno):
    results = conn_bd.busca_relatorio(where="aluno", value=nusp_aluno)
    return results

@app.route('/detalhes_relatorio/<relatorio_id>', methods=['GET'])
def get_detalhes_relatorio(relatorio_id):
    results = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    return results

@app.route('/feedback/<nusp_aluno>')
def feedback(nusp_aluno):
    return render_template('feedback.html', nusp_aluno=nusp_aluno)

@app.route('/novo_relatorio/<nusp_aluno>', methods=['GET', 'POST'])
def forms_relatorio(nusp_aluno):
    if request.method == 'POST':
        dados = request.json

        atividades_resp = dados.get('atividades_resp')
        pesquisas_resp = dados.get('pesquisas_resp')
        observacoes_resp = dados.get('observacoes_resp')
        dificuldade = dados.get('dificuldade')
        escrita = dados.get('escrita')
        aval = dados.get('aval')
        publicados = dados.get('publicados')

        return conn_bd.inserir_relatorio(nusp_aluno, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, escrita, aval, publicados, titulo="Titulo")

    return render_template('formulario_relatorio_aluno.html', nusp_aluno=nusp_aluno)

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
            return redirect(url_for('index', nusp_aluno=nusp))  
           
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
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