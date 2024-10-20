from flask import jsonify
import psycopg2
from datetime import datetime
import env


def get_db_conn():
    """
    Cria conexão ao banco de dados.

    :return: Objeto de conexão
    """
    conn = psycopg2.connect(
        host=env.host,
        database=env.database,
        user=env.user,
        password=env.password
    )
    return conn

def busca_aluno(where=None, value=None):
    """
    Realiza busca na tabela de aluno, podendo ter filtros ou não.

    :param where: Nome da coluna para realização do filtro
    :param value: Valor a ser filtrado 
    :return: Resultado da query
    """ 
    
    query = "SELECT * FROM alunos"
    if where: 
        query += f" WHERE {where} = {value}"
    
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()

    cur.close()
    conn.close()

    dados_aluno = []

    for dados in result:
        dados_aluno.append({
            'nusp': dados[0],
            'nome': dados[1],
            'email': dados[2],
            'orientador': dados[3],
            'lattes': dados[4],
            'curso': dados[5],
            'data_matricula': dados[6],
            'disc_aprov': dados[7],
            'disc_reprov': dados[8],
            'data_exqualif': dados[9],
            'data_exprof': dados[10],
            'data_dissert': dados[11],
        })
    
    return jsonify({'dados_aluno': dados_aluno})

def busca_relatorio(where=None, value=None):
    """
    Realiza busca na tabela de relatórios, podendo ter filtros ou não.

    :param where: Nome da coluna para realização do filtro
    :param value: Valor a ser filtrado 
    :return: Resultado da query
    """
    query = "SELECT * FROM relatorios"
    if where: 
        query += f" WHERE {where} = {value}"
    
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()

    cur.close()
    conn.close()

    relatorios = []

    for relatorio in result:
        relatorios.append({
            'id': relatorio[0],
            'titulo': relatorio[1],
            'texto': relatorio[2],
            'data_envio': relatorio[3],
            'nota_professor': relatorio[4],
            'nota_ccp': relatorio[5],
            'parecer_professor': relatorio[6],
            'parecer_ccp': relatorio[7],
            'aluno': relatorio[8],
            'orientador': relatorio[9] 
        })
    
    return jsonify({'relatorios': relatorios})

def inserir_relatorio(nusp_aluno, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, escrita, aval, publicados):
    """
    Insere um novo relatório no banco de dados.

    :param nusp_aluno: NUSP do aluno
    :param atividades_resp: Respostas sobre atividades
    :param pesquisas_resp: Respostas sobre pesquisas
    :param observacoes_resp: Observações adicionais
    :param dificuldade: Dificuldade enfrentada
    :param escrita: Resposta sobre artigos em fase de escrita
    :param aval: Resposta sobre artigos submetidos e em avaliação
    :param publicados: Resposta sobre artigos aceitos ou publicados
    """
    query = """
    INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    conn = get_db_conn()
    cur = conn.cursor()
    
    titulo = "Relatório"
    data_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    texto = f"""
    Atividades: {atividades_resp}
    Pesquisas: {pesquisas_resp}
    Observações: {observacoes_resp}
    Dificuldade: {dificuldade}
    """
    # Escrita: {int(escrita.split('-')[-1])}
    # Avaliação: {int(aval.split('-')[-1])}
    # Publicados: {int(publicados.split('-')[-1])}


    # dados_aluno = busca_aluno(where='nusp', value=nusp_aluno)
    # orientador = dados_aluno[0]['orientador'] if dados_aluno else None

    cur.execute(query, (titulo, texto, data_envio, "Aguardando", "Aguardando", "Parecer ainda não enviado", "Parecer ainda não enviado", nusp_aluno, "1"))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Relatório adicionado com sucesso!"}), 201