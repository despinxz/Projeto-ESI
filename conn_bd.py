from flask import jsonify
import psycopg2
from datetime import datetime


def get_db_conn():
    """
    Cria conexão ao banco de dados.

    :return: Objeto de conexão
    """
    conn = psycopg2.connect(
        host='localhost',
        database='posgraduacao',
        user='postgres',
        password='12345678'
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
            'data_nasc': dados[3],
            'rg': dados[4],
            'local_nasc': dados[5],
            'nacionalidade': dados[6],
            'lattes': dados[7]
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
            'atividades_resp': relatorio[2],
            'pesquisas_resp': relatorio[3],
            'observacoes_resp': relatorio[4],
            'dificuldades': relatorio[5],
            'data_envio': relatorio[6],
            'nota_professor': relatorio[7],
            'nota_ccp': relatorio[8],
            'parecer_professor': relatorio[9],
            'parecer_ccp': relatorio[10],
            'aluno': relatorio[11],
            'orientador': relatorio[12],
            'escrita': relatorio[13],
            'aval': relatorio[14],
            'publicados': relatorio[15]
        })
    
    return jsonify({'relatorios': relatorios})

def salvar_parecer_prof(id_relatorio, parecer, nivel):
    query = """
        UPDATE relatorios
        SET parecer_professor = %s, nota_professor = %s
        WHERE id = %s
        """
    
    conn = get_db_conn()
    cur = conn.cursor()

    try:
        cur.execute(query, (parecer,nivel,id_relatorio))
        conn.commit()

    except psycopg2.Error as e:
        print(f"Erro ao inserir parecer: {e}")
        return False

    cur.close()
    conn.close()

    return True

def salvar_parecer_ccp(nusp_aluno, parecer, nivel):
    query = """
        UPDATE relatorios
        SET parecer_ccp = %s, nota_ccp = %s
        WHERE aluno = %s
        """
    
    conn = get_db_conn()
    cur = conn.cursor()

    try:
        cur.execute(query, (parecer,nivel,nusp_aluno))
        conn.commit()

    except psycopg2.Error as e:
        print(f"Erro ao inserir parecer: {e}")
        return False

    cur.close()
    conn.close()

    return True

def inserir_relatorio(nusp_aluno, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, escrita, aval, publicados, titulo):
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
    INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    conn = get_db_conn()
    cur = conn.cursor()

    dados_aluno = busca_aluno(where='nusp', value=nusp_aluno)
    orientador = dados_aluno[0]['orientador'] if dados_aluno else None

    data_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    escrita = escrita.split('-')[-1]
    aval = aval.split('-')[-1]
    publicados = publicados.split('-')[-1]

    cur.execute(query, (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, "Aguardando", "Aguardando", "Aguardando", "Aguardando", nusp_aluno, orientador, escrita, aval, publicados))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Relatório adicionado com sucesso!"}), 201