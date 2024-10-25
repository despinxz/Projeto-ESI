from flask import Flask, request, render_template, jsonify 
import conn_bd
import psycopg2 

app = Flask(__name__)

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

        return conn_bd.inserir_relatorio(nusp_aluno, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, escrita, aval, publicados)

    return render_template('formulario_relatorio_aluno.html', nusp_aluno=nusp_aluno)

if __name__ == '__main__':
    app.run(debug=True)