from flask import jsonify
import psycopg2

def get_db_conn():
    """
    Cria conexão ao banco de dados.

    :return: Objeto de conexão
    """
    conn = psycopg2.connect(
        host='localhost',
        database='posgraduacao',
        user='postgres',
        password='15262435'
    )
    return conn

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

