from flask import Blueprint, request, jsonify, render_template
import conn_bd

aluno = Blueprint('aluno', __name__, template_folder='templates')

@aluno.route('/<nusp>')
def index(nusp):
    return render_template('index_aluno.html', nusp=nusp)

@aluno.route('/tabela_relatorios/<nusp>')
def tabela_relatorios(nusp):
    return render_template('tabela_relatorios_aluno.html', nusp=nusp)

@aluno.route('/relatorio/<id>')
def detalhes_relatorio(id):
    return render_template('detalhes_relatorio_aluno.html', relatorio_id=id)

@aluno.route('/editar_relatorio/<id>')
def editar_relatorio(id):
    return render_template('editar_relatorio_aluno.html', relatorio_id=id)

@aluno.route('/formulario/<nusp>')
def render_forms_relatorio(nusp):
    return render_template('formulario_relatorio_aluno.html', nusp=nusp)

@aluno.route('/relatorios/<nusp>', methods=['GET'])
def get_relatorios_aluno(nusp):
    results = conn_bd.busca_relatorio(where="aluno", value=nusp)
    return results

@aluno.route('/detalhes_relatorio/<id>', methods=['GET'])
def get_detalhes_relatorio(id):
    results = conn_bd.busca_relatorio(where="id", value=id)
    return results

@aluno.route('/data_entrega', methods=['GET'])
def get_data_entrega():
    results = conn_bd.data_entrega()
    return results

@aluno.route('/novo_relatorio/<nusp>', methods=['POST'])
def forms_relatorio(nusp):
    dados = request.json  # Recebe os dados no formato JSON

    atividades_resp = dados.get('atividades_resp')
    pesquisas_resp = dados.get('pesquisas_resp')
    observacoes_resp = dados.get('observacoes_resp')
    dificuldade = dados.get('dificuldade')
    escrita = dados.get('escrita')
    aval = dados.get('aval')
    publicados = dados.get('publicados')
    data_limite = dados.get('data_limite')

    sucesso = conn_bd.inserir_relatorio(nusp, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, escrita, aval, publicados, titulo="Titulo", data_limite=data_limite)
    if sucesso:
        return {"message": "Relatório enviado com sucesso!"}, 200
    else:
        return {"error": "Erro ao salvar relatório."}, 500

@aluno.route('/enviar_edicao_relatorio/<id>', methods=['PUT'])
def enviar_edicao_relatorio(id):
    dados = request.json

    atividades_resp = dados.get('atividades_resp')
    pesquisas_resp = dados.get('pesquisas_resp')
    observacoes_resp = dados.get('observacoes_resp')
    dificuldade = dados.get('dificuldade')
    escrita = dados.get('escrita')
    aval = dados.get('aval')
    publicados = dados.get('publicados')
    data_limite = dados.get('data_limite')

    sucesso = conn_bd.editar_relatorio(id, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, escrita, aval, publicados, titulo="Titulo", data_limite=data_limite)
    if sucesso:
        return {"message": "Relatório enviado com sucesso!"}, 200
    else:
        return {"error": "Erro ao salvar relatório."}, 500
