from flask import Blueprint, request, render_template, jsonify
import conn_bd

professor = Blueprint('professor', __name__, template_folder='templates')

@professor.route('/<nusp>')
def index(nusp):
    return render_template('index_professor.html', nusp=nusp)

@professor.route('/tabela_relatorios/<nusp>')
def tabela_relatorios(nusp):
    return render_template('tabela_relatorios_professor.html', nusp=nusp)

@professor.route('/relatorio/<id>')
def detalhes_relatorio(id):
    return render_template('detalhes_relatorio_professor.html', relatorio_id=id)

@professor.route('/tabela_relatorios/relatorios/<nusp>', methods=['GET'])
def get_relatorios_professor(nusp):
    results = conn_bd.busca_relatorio(where="orientador", value=nusp)
    return results

@professor.route('/detalhes_relatorio/<relatorio_id>', methods=['GET'])
def get_detalhes_relatorio(relatorio_id):
    results = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    return results

@professor.route('/feedback_professor/<relatorio_id>', methods=['GET'])
def get_relatorio_feedback(relatorio_id):
    detalhes_aluno = conn_bd.busca_detalhes_aluno(value=relatorio_id)

    if not detalhes_aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    aluno = detalhes_aluno[0]

    return render_template('feedback_professor.html',
                           nusp=aluno['nusp'],
                           nome=aluno['nome'],
                           data_envio=aluno['data_envio'],
                           lattes=aluno['lattes'],
                           atividades_academicas=aluno['atividades_academicas'],
                           resumo_pesquisa=aluno['resumo_pesquisa']
                           )

@professor.route('/feedback_professor/<relatorio_id>/save', methods=['POST'])
def salvar_parecer(relatorio_id):
    dados = request.get_json()
    parecer = dados.get('parecer_resp')
    nivel = dados.get('nivel')

    if not parecer or not nivel:
        return jsonify({"error": "Dados incompletos"}), 400

    if conn_bd.salvar_parecer_prof(relatorio_id, parecer, nivel):
        return jsonify({"sucesso": True, "mensagem": "Parecer salvo com sucesso!"}), 200
    else:
        return jsonify({"error": "Erro ao salvar parecer"}), 500
