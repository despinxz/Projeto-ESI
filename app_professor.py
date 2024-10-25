from flask import Flask, request, render_template, jsonify 
import conn_bd
import psycopg2 

app = Flask(__name__)

@app.route('/<nusp_professor>')
def index(nusp_professor):
    return render_template('index_professor.html', nusp_professor=nusp_professor)

@app.route('/tabela_relatorios/<nusp_professor>')
def tabela_relatorios(nusp_professor):
    return render_template('tabela_relatorios_professor.html', nusp_aluno=nusp_professor)

@app.route('/relatorio/<id>')
def detalhes_relatorio(id):
    return render_template('detalhes_relatorio_professor.html', relatorio_id=id)

@app.route('/relatorios/<nusp_professor>', methods=['GET'])
def get_relatorios_professor(nusp_professor):
    results = conn_bd.busca_relatorio(where="orientador", value=nusp_professor)
    return results

@app.route('/detalhes_relatorio/<relatorio_id>', methods=['GET'])
def get_detalhes_relatorio(relatorio_id):
    results = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    return results

# @app.route('/feedback_professor/<nusp_aluno>', methods=['GET'])
# def get_detalhes_aluno(nusp_aluno):
    # detalhes_aluno = conn_bd.busca_detalhes_aluno(where="nusp", value=nusp_aluno)

    # if not detalhes_aluno:
    #     return jsonify({"error": "Aluno não encontrado"}), 404

    # aluno = detalhes_aluno[0]

#     return render_template('feedback_professor.html',
                        #    nusp_aluno=aluno['nusp'],
                        #    nome=aluno['nome'],
                        #    data_envio=aluno['data_envio'],
                        #    curso=aluno['curso'],
                        #    lattes=aluno['lattes'],
                        #    aprovacoes=aluno['aprovacoes'],
                        #    reprovacoes=aluno['reprovacoes'],
                        #    atividades_academicas=aluno['atividades_academicas'],
                        #    resumo_pesquisa=aluno['resumo_pesquisa'])

# @app.route('/feedback_professor/<nusp_aluno>/save', methods=['POST'])
# def salvar_parecer(nusp_aluno):
#     dados = request.get_json()
#     parecer = dados.get('parecer_resp')
#     nivel = dados.get('nivel')

#     if not parecer or not nivel:
#         return jsonify({"error": "Dados incompletos"}), 400

#     if conn_bd.salvar_parecer_prof(nusp_aluno, parecer, nivel):
#         return jsonify({"sucesso": True, "mensagem": "Parecer salvo com sucesso!"}), 200
#     else:
#         return jsonify({"error": "Erro ao salvar parecer"}), 500
    

@app.route('/feedback_professor/<relatorio_id>', methods=['GET', 'POST'])
def forms_relatorio(relatorio_id):
    if request.method == 'POST':
        dados = request.json

        parecer = dados.get('parecer_resp')
        nivel = dados.get('nivel')

        return conn_bd.inserir_relatorio(conn_bd.salvar_parecer_prof(parecer, nivel, relatorio_id))

    # detalhes_curso = conn_bd.busca_curso(where=, value)
    # curso = detalhes_curso[0]

    detalhes_relatorio = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    relatorio = detalhes_relatorio[0]

    nusp_aluno = relatorio['aluno']
    
    detalhes_aluno = conn_bd.busca_aluno(where="nusp", value=nusp_aluno)
    aluno = detalhes_aluno[0]

    return render_template('feedback_professor.html', relatorio_id=relatorio_id,
                           nusp_aluno=aluno['nusp'],
                           nome=aluno['nome'],
                           data_envio=relatorio['data_envio'],
                           curso=curso['nome'],
                           lattes=aluno['lattes'],
                           aprovacoes=curso['aprovacoes'],
                           reprovacoes=curso['reprovacoes'],
                           atividades_resp=relatorio['atividades_resp'],
                           observacoes_resp=relatorio['observacoes_resp'])

if __name__ == '__main__':
    app.run(debug=True)