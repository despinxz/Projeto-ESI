from flask import Blueprint, request, render_template, jsonify
import conn_bd

ccp = Blueprint('ccp', __name__, template_folder='templates')

@ccp.route('/<nusp>')
def index(nusp):
    return render_template('index_ccp.html', nusp=nusp)

@ccp.route('/tabela_relatorios')
def tabela_relatorios():
    return render_template('tabela_relatorios_ccp.html')

@ccp.route('/tabela_alunos')
def tabela_alunos():
    return render_template('tabela_alunos_ccp.html')

@ccp.route('/relatorio/<id>')
def detalhes_relatorio(id):
    return render_template('detalhes_relatorio_ccp.html', relatorio_id=id)

@ccp.route('/aluno/<nusp>')
def detalhes_aluno(nusp):
    return render_template('detalhes_aluno_ccp.html', nusp=nusp)

@ccp.route('/relatorios', methods=['GET'])
def get_relatorios_ccp():
    results = conn_bd.busca_relatorio()
    return results

@ccp.route('/alunos', methods=['GET'])
def get_alunos_ccp():
    results = conn_bd.busca_aluno()
    return results

@ccp.route('/detalhes_relatorio/<relatorio_id>', methods=['GET', 'POST'])
def get_detalhes_relatorio(relatorio_id):
    results = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    return results

@ccp.route('/detalhes_aluno/<nusp>', methods=['GET', 'POST'])
def get_info_aluno(nusp):
    results = conn_bd.busca_aluno(where='nusp', value=nusp)
    return results

@ccp.route('/feedback_ccp/<relatorio_id>', methods=['GET'])
def get_relatorio_feedback(relatorio_id):
    detalhes_aluno = conn_bd.busca_detalhes_aluno(value=relatorio_id)

    if not detalhes_aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    aluno = detalhes_aluno[0]

    return render_template('feedback_ccp.html',
                           nusp_aluno=aluno['nusp'],
                           nome=aluno['nome'],
                           data_envio=aluno['data_envio'],
                           lattes=aluno['lattes'],
                           parecer_professor=aluno['parecer_professor'],
                           atividades_academicas=aluno['atividades_academicas'],
                           resumo_pesquisa=aluno['resumo_pesquisa'])

@ccp.route('/feedback_ccp/<relatorio_id>/save', methods=['POST'])
def salvar_parecer(relatorio_id):
    dados = request.get_json()
    parecer = dados.get('parecer_resp')
    nivel = dados.get('nivel')

    if not parecer or not nivel:
        return jsonify({"error": "Dados incompletos"}), 400

    if conn_bd.salvar_parecer_ccp(relatorio_id, parecer, nivel):
        return jsonify({"sucesso": True, "mensagem": "Parecer salvo com sucesso!"}), 200
    else:
        return jsonify({"error": "Erro ao salvar parecer"}), 500

@ccp.route('/atualizar_data', methods=['POST'])
def atualizar_data():
    dados = request.get_json() 
    data_selecionada = dados.get('date')

    if not data_selecionada:
        return jsonify({"error": "Dados incompletos. Certifique-se de enviar 'date'."}), 400

    # Atualiza a data no banco de dados
    sucesso = conn_bd.atualizar_data_relatorio(data_selecionada)

    if sucesso:
        return jsonify({"sucesso": True, "mensagem": "Data atualizada com sucesso!"}), 200
    else:
        return jsonify({"error": "Erro ao atualizar a data no banco de dados."}), 500
    
@ccp.route('/desligar_aluno/<nusp>', methods=['POST'])
def desligar_aluno(nusp):
    sucesso = conn_bd.desligar_aluno(nusp)  
    if sucesso:
        return jsonify({"mensagem": "Aluno desligado com sucesso!"}), 200
    else:
        return jsonify({"error": "Erro ao desligar o aluno."}), 500
