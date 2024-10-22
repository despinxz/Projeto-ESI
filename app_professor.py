from flask import Flask, request, render_template, jsonify 
import conn_bd
import psycopg2 

app = Flask(__name__)

@app.route('/<nusp_professor>')
def index(nusp_professor):
    return render_template('index_professor.html', nusp_professor=nusp_professor)

@app.route('/relatorio/<id>')
def detalhes_relatorio(id):
    return render_template('detalhes_relatorio_aluno.html', relatorio_id=id)

@app.route('/relatorios/<nusp_professor>', methods=['GET'])
def get_relatorios_professor(nusp_professor):
    results = conn_bd.busca_relatorio(where="orientador", value=nusp_professor)
    return results

@app.route('/detalhes_relatorio/<relatorio_id>', methods=['GET', 'POST'])
def get_detalhes_relatorio(relatorio_id):
    results = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    return results

@app.route('/feedback/<nusp_aluno>', methods=['GET'])
def get_detalhes_aluno(nusp_aluno):
    detalhes_aluno = conn_bd.busca_detalhes_aluno(where="nusp", value=nusp_aluno)

    if not detalhes_aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    aluno = detalhes_aluno[0]

    return render_template('feedback.html',
                           nusp_aluno=aluno['nusp'],
                           nome=aluno['nome'],
                           data_envio=aluno['data_envio'],
                           curso=aluno['curso'],
                           lattes=aluno['lattes'],
                           aprovacoes=aluno['aprovacoes'],
                           reprovacoes=aluno['reprovacoes'],
                           atividades_academicas=aluno['atividades_academicas'],
                           resumo_pesquisa=aluno['resumo_pesquisa'])

@app.route('/feedback/<nusp_aluno>/save', methods=['POST'])
def salvar_parecer(nusp_aluno):
    dados = request.get_json()
    parecer = dados.get('parecer_resp')
    nivel = dados.get('nivel')

    if not parecer or not nivel:
        return jsonify({"error": "Dados incompletos"}), 400

    if conn_bd.salvar_parecer_prof(nusp_aluno, parecer, nivel):
        return jsonify({"sucesso": True, "mensagem": "Parecer salvo com sucesso!"}), 200
    else:
        return jsonify({"error": "Erro ao salvar parecer"}), 500

if __name__ == '__main__':
    app.run(debug=True)