from flask import Blueprint, request, render_template, jsonify
import conn_bd

ccp = Blueprint('ccp', __name__, template_folder='templates')

@ccp.route('/<nusp>')
def index(nusp):
    return render_template('index_ccp.html', nusp=nusp)

@ccp.route('/tabela_relatorios')
def tabela_relatorios():
    return render_template('tabela_relatorios_ccp.html')

@ccp.route('/relatorio/<id>')
def detalhes_relatorio(id):
    return render_template('detalhes_relatorio_ccp.html', relatorio_id=id)

@ccp.route('/relatorios', methods=['GET'])
def get_relatorios_ccp():
    results = conn_bd.busca_relatorio()
    return results

@ccp.route('/detalhes_relatorio/<relatorio_id>', methods=['GET', 'POST'])
def get_detalhes_relatorio(relatorio_id):
    results = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    return results

@ccp.route('/feedback_ccp/<nusp_aluno>', methods=['GET'])
def get_detalhes_aluno(nusp_aluno):
    detalhes_aluno = conn_bd.busca_detalhes_aluno(where="nusp", value=nusp_aluno)

    if not detalhes_aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    aluno = detalhes_aluno[0]

    return render_template('feedback_ccp.html',
                           nusp_aluno=aluno['nusp'],
                           nome=aluno['nome'],
                           data_envio=aluno['data_envio'],
                           curso=aluno['curso'],
                           lattes=aluno['lattes'],
                           aprovacoes=aluno['aprovacoes'],
                           reprovacoes=aluno['reprovacoes'],
                           parecer_professor=aluno['parecer_professor'],
                           atividades_academicas=aluno['atividades_academicas'],
                           resumo_pesquisa=aluno['resumo_pesquisa'])

@ccp.route('/feedback_ccp/<nusp_aluno>/save', methods=['POST'])
def salvar_parecer(nusp_aluno):
    dados = request.get_json()
    parecer = dados.get('parecer_resp')
    nivel = dados.get('nivel')

    if not parecer or not nivel:
        return jsonify({"error": "Dados incompletos"}), 400

    if conn_bd.salvar_parecer_ccp(nusp_aluno, parecer, nivel):
        return jsonify({"sucesso": True, "mensagem": "Parecer salvo com sucesso!"}), 200
    else:
        return jsonify({"error": "Erro ao salvar parecer"}), 500
