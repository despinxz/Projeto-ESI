from flask import jsonify, flash
import psycopg2
from datetime import datetime
import json
import env


def get_db_conn():
    """
    Cria conexão ao banco de dados.

    :return: Objeto de conexão
    """
    conn = psycopg2.connect(
        host=env.DB_HOST,
        database='posgraduacao',
        user=env.DB_USER,
        password=env.DB_PASSWORD
    )
    return conn

def get_nome_curso(curso):
    """
    Retorna o nome do curso a partir do seu ID.

    :param curso: ID do curso
    :return: Nome do curso
    """
    query = f"""
        SELECT nome_curso
        FROM cursos
        WHERE id = {curso}
    """

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()

    cur.close()
    conn.close()

    dados = []

    for dados in result:
        dados.append({
            'nome_curso': dados[0]
        })
    
    return jsonify({'dados': dados})


def num_materias_reprovadas(nusp, curso):
    """
    Retorna o número de matérias reprovadas por um aluno em um curso.

    :param nusp: NUSP do aluno
    :param curso: Curso do aluno
    :return: Número de matérias reprovadas
    """

    query = f"""
        SELECT 
        COUNT(DISTINCT cursos_disciplinas_reprovadas.id_disciplina) AS disciplinas_reprovadas
        FROM 
        alunos
        JOIN 
        cursos ON cursos.aluno = alunos.nusp
        JOIN 
        cursos_disciplinas_reprovadas ON cursos.id = cursos_disciplinas_reprovadas.id_curso
        WHERE 
        alunos.nusp = {nusp}
        AND cursos.id = {curso}
        GROUP BY 
        alunos.nusp, cursos.id;
    """

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()

    cur.close()
    conn.close()

    # refatorar depois
    dados = []

    for dados in result:
        dados.append({
            'disciplinas_reprovadas': dados[0]
        })
    
    return jsonify({'dados': dados})

def num_materias_aprovadas(nusp, curso):
    """
    Retorna o número de matérias aprovadas por um aluno em um curso.

    :param nusp: NUSP do aluno
    :param curso: Curso do aluno
    :return: Número de matérias aprovadas
    """

    query = f"""
        SELECT 
        COUNT(DISTINCT cursos_disciplinas_aprovadas.id_disciplina) AS disciplinas_aprovadas
        FROM 
        alunos
        JOIN 
        cursos ON cursos.aluno = alunos.nusp
        JOIN 
        cursos_disciplinas_aprovadas ON cursos.id = cursos_disciplinas_aprovadas.id_curso
        WHERE 
        alunos.nusp = {nusp}
        AND cursos.id = {curso}
        GROUP BY 
        alunos.nusp, cursos.id;
    """

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()

    cur.close()
    conn.close()

    # refatorar depois
    dados = []

    for dados in result:
        dados.append({
            'disciplinas_aprovadas': dados[0]
        })
    
    return jsonify({'dados': dados})

def busca_orientador(nusp_aluno=None):
    """
    Realiza busca na tabela de cursos e verifica qual é o orientador do aluno com base no nusp do aluno

    :param where: Nusp do aluno
    :param value: Valor a ser filtrado
    :return: Resultado da query
    """

    if not nusp_aluno:
        return jsonify({'error': 'Número USP do aluno é obrigatório'}), 400
    
    query = """
        SELECT orientador
        FROM alunos a
        WHERE a.nusp = %s
    """
    
    conn = get_db_conn()
    cur = conn.cursor()
    
    cur.execute(query, (nusp_aluno,))
    result = cur.fetchone()  # Assume que o orientador é retornado na primeira coluna
    
    cur.close()
    conn.close()
    
    if result:
        return result[0]  # Retorna o orientador encontrado
    else:
        return None  # Caso não encontre orientador

def busca_aluno(where=None, value=None):
    """
    Realiza busca na tabela de aluno e verifica o desempenho com base nos relatórios enviados.

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

    dados_aluno = []

    for dados in result:
        nusp = dados[0]

        # Query para buscar os dois relatórios mais recentes do aluno
        relatorios_query = f"""
            SELECT nota_ccp
            FROM relatorios
            WHERE aluno = {nusp}
            ORDER BY data_envio DESC
            LIMIT 2
        """
        cur.execute(relatorios_query)
        relatorios = cur.fetchall()

        # Verificar as duas últimas notas
        notas = [relatorio[0] for relatorio in relatorios]
        baixo_desempenho = notas.count('Insatisfatório') == 2

        dados_aluno.append({
            'nusp': dados[0],
            'nome': dados[1],
            'email': dados[2],
            'data_nasc': dados[4],
            'rg': dados[5],
            'local_nasc': dados[6],
            'nacionalidade': dados[7],
            'lattes': dados[8],
            'status_aluno': dados[10],
            'baixo_desempenho': baixo_desempenho,
            'ultimas_notas': notas  # Inclui as últimas duas notas no JSON
        })

    cur.close()
    conn.close()

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
            'publicados': relatorio[15],
            'data_limite': relatorio[16]
        })
    
    return jsonify({'relatorios': relatorios})

def busca_detalhes_aluno(where=None, value=None):
    query = """
    SELECT a.nome, a.nusp, r.data_envio, a.lattes, r.parecer_professor, r.atividades_resp, r.pesquisas_resp
    FROM alunos a LEFT JOIN relatorios r ON a.nusp = r.aluno"""
    if where: 
        query += f" WHERE r.id = {value}"

    conn = get_db_conn()
    cur = conn.cursor()

    cur.execute(query)

    result = cur.fetchall()

    cur.close()
    conn.close()

    # Caso o resultado seja None (nenhum aluno encontrado)
    if result is None:
        return None
    
    detalhes_aluno =[]

    for detalhe_aluno in result:
        detalhes_aluno.append({
        'nome': detalhe_aluno[0],
        'nusp': detalhe_aluno[1],
        'data_envio': detalhe_aluno[2],
        'lattes': detalhe_aluno[3],
        'parecer_professor': detalhe_aluno[4],
        'atividades_academicas': detalhe_aluno[5],
        'resumo_pesquisa': detalhe_aluno[6]
    })

    return (detalhes_aluno)

def salvar_parecer_prof(id, parecer, nivel):
    query = """
        UPDATE relatorios
        SET parecer_professor = %s, nota_professor = %s
        WHERE id = %s
        """
    
    conn = get_db_conn()
    cur = conn.cursor()

    try:
        cur.execute(query, (parecer,nivel,id))
        conn.commit()

    except psycopg2.Error as e:
        print(f"Erro ao inserir parecer: {e}")
        return False

    cur.close()
    conn.close()

    return True

def salvar_parecer_ccp(id, parecer, nivel):
    query = """
        UPDATE relatorios
        SET parecer_ccp = %s, nota_ccp = %s
        WHERE id = %s
        """
    
    conn = get_db_conn()
    cur = conn.cursor()

    try:
        cur.execute(query, (parecer,nivel,id))
        conn.commit()

    except psycopg2.Error as e:
        print(f"Erro ao inserir parecer: {e}")
        return False

    cur.close()
    conn.close()

    return True

def inserir_relatorio(nusp, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, escrita, aval, publicados, titulo, data_limite):
    """
    Insere um novo relatório no banco de dados.

    :param nusp: NUSP do aluno
    :param atividades_resp: Respostas sobre atividades
    :param pesquisas_resp: Respostas sobre pesquisas
    :param observacoes_resp: Observações adicionais
    :param dificuldade: Dificuldade enfrentada
    :param escrita: Resposta sobre artigos em fase de escrita
    :param aval: Resposta sobre artigos submetidos e em avaliação
    :param publicados: Resposta sobre artigos aceitos ou publicados
    """
    query = """
    INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados, data_limite) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    conn = get_db_conn()
    cur = conn.cursor()

    dados_aluno = busca_aluno(where='nusp', value=nusp)
    orientador = busca_orientador(nusp_aluno=nusp)

    data_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    escrita = str(escrita.split('-')[-1])
    aval = str(aval.split('-')[-1])
    publicados = str(publicados.split('-')[-1])

    if dificuldade == 'diff_sim':
        dificuldade = 'Sim'
    else:
        dificuldade = 'Não'

    cur.execute(query, (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, "Aguardando", "Aguardando", "Parecer ainda não enviado", "Parecer ainda não enviado", nusp, orientador, escrita, aval, publicados, data_limite))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Relatório adicionado com sucesso!"}), 201

def verificar_login(tipo, id, senha):
    conn = get_db_conn()
    cur = conn.cursor()

    if tipo == 'ccp':
        query = "SELECT * FROM ccp WHERE nusp = %s AND senha = %s"
    elif tipo == 'aluno':
        query = "SELECT * FROM alunos WHERE nusp = %s AND senha = %s"
    elif tipo == 'professor':
        query = "SELECT * FROM professores WHERE nusp = %s AND senha = %s"
    
    try:
        cur.execute(query, (id, senha))
        result = cur.fetchone()

        if result:
            flash('Login realizado com sucesso!', 'success')
            return True

        else:
            flash('Credenciais incorretas. Tente novamente.', 'error')
            return False


    except Exception as e:
        flash(f'Ocorreu um erro: {str(e)}', 'error')
        return False

    finally:
        cur.close()
        conn.close()


def cadastrar_usuario(tipo, dados):
    conn = get_db_conn()
    cur = conn.cursor()

    try:
        if tipo == 'ccp':
            cur.execute("SELECT * FROM ccp WHERE nusp = %s", (dados['nusp'],))
            result = cur.fetchone()
            if result:
                flash('Este usuário CCP já existe.', 'error')
                return False
            
            cur.execute("INSERT INTO ccp (nusp, nome, senha) VALUES (%s, %s, %s)", 
                        (dados['nusp'], dados['nome'], dados['senha']))

        elif tipo == 'aluno':
            cur.execute("SELECT * FROM alunos WHERE nusp = %s", (dados['nusp'],))
            result = cur.fetchone()
            if result:
                flash('Este aluno já está cadastrado.', 'error')
                return False

            cur.execute(""" 
                INSERT INTO alunos (nusp, nome, email, senha, data_nasc, rg, local_nasc, nacionalidade, lattes, orientador, status_aluno) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (dados['nusp'], dados['nome'], dados['email'], dados['senha'],
                  dados['data_nasc'], dados['rg'], dados['local_nasc'], dados['nacionalidade'], dados['lattes'], dados['orientador'], 'Ativo'))

        elif tipo == 'professor':
            cur.execute("SELECT * FROM professores WHERE nusp = %s", (dados['nusp'],))
            result = cur.fetchone()
            if result:
                flash('Este professor já está cadastrado.', 'error')
                return False

            cur.execute("INSERT INTO professores (nusp, nome, senha) VALUES (%s, %s, %s)", 
                        (dados['nusp'], dados['nome'], dados['senha']))

        conn.commit()
        flash('Cadastro realizado com sucesso! Agora você pode fazer o login.', 'success')
        return True

    except Exception as e:
        flash(f'Ocorreu um erro: {str(e)}', 'error')
        return False

    finally:
        cur.close()
        conn.close()

def atualizar_data_relatorio(nova_data):
    query = f"""
        UPDATE data_entrega_relatorio
        SET data_entrega_relatorio = DATE('{nova_data}') + INTERVAL '1 day'
        WHERE id = '1';

    """
    try:
        conn = get_db_conn()  
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao atualizar data: {e}")
        return False
    finally:
        if conn:
            conn.close()

def data_entrega():
    """
    Retorna a data de entrega geral dos relatórios.

    :return: Data de entrega no formato JSON.
    """
    query = """
        SELECT data_entrega_relatorio
        FROM data_entrega_relatorio
        WHERE id = '1'
    """

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(query)

    # Obtem apenas o primeiro resultado
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return jsonify({'date': result[0]})  # Retorna o campo diretamente como JSON
    else:
        return jsonify({'error': 'Data não encontrada.'}), 404

def desligar_aluno(nusp):
    """
    Atualiza o status do aluno para 'Inativo' na tabela alunos.

    :param nusp: Número USP do aluno a ser desligado.
    :return: JSON indicando sucesso ou falha da operação.
    """
    query = """
        UPDATE alunos
        SET status_aluno = 'Inativo'
        WHERE nusp = %s
    """
    
    conn = get_db_conn()
    cur = conn.cursor()
    
    try:
        cur.execute(query, (nusp,))  
        conn.commit() 
        
        cur.close()
        conn.close()
        
        return jsonify({"mensagem": "Aluno desligado com sucesso!"}), 200
    except Exception as e:
        
        conn.rollback()  
        cur.close()
        conn.close()
        
        return jsonify({"error": f"Erro ao desligar o aluno: {str(e)}"}), 500

def editar_relatorio(id, atividades_resp="", pesquisas_resp="", observacoes_resp="", dificuldade="", escrita="", aval="", publicados="", titulo="", data_limite=""):
    """
    Atualiza um relatório existente no banco de dados com base no ID. 
    Apenas os parâmetros fornecidos (não vazios) serão atualizados.

    :param id: ID do relatório a ser atualizado
    :param atividades_resp: Respostas sobre atividades
    :param pesquisas_resp: Respostas sobre pesquisas
    :param observacoes_resp: Observações adicionais
    :param dificuldade: Dificuldade enfrentada
    :param escrita: Resposta sobre artigos em fase de escrita
    :param aval: Resposta sobre artigos submetidos e em avaliação
    :param publicados: Resposta sobre artigos aceitos ou publicados
    :param titulo: Título do relatório
    :param data_limite: Data limite para entrega
    """
    conn = get_db_conn()
    cur = conn.cursor()

    data_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Mapeia os parâmetros em pares coluna=valor
    campos = {
        "atividades_resp": atividades_resp,
        "pesquisas_resp": pesquisas_resp,
        "observacoes_resp": observacoes_resp,
        "dificuldade": dificuldade,
        "data_envio": data_envio,
        "escrita": escrita,
        "aval": aval,
        "publicados": publicados,
        "titulo": titulo,
        "data_limite": data_limite
    }

    # Filtra os campos não vazios
    campos_nao_vazios = {coluna: valor for coluna, valor in campos.items() if valor}

    if not campos_nao_vazios:
        return jsonify({"error": "Nenhum campo para atualizar."}), 400

    # Constrói a query dinamicamente
    set_clause = ", ".join([f"{coluna} = %s" for coluna in campos_nao_vazios.keys()])
    query = f"UPDATE relatorios SET {set_clause} WHERE id = %s"

    # Executa a query com os valores
    valores = list(campos_nao_vazios.values()) + [id]
    cur.execute(query, valores)

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Relatório atualizado com sucesso!"}), 200

