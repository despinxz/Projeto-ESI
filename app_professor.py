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

@app.route('/detalhes_relatorio/<relatorio_id>', methods=['GET'])
def get_detalhes_relatorio(relatorio_id):
    results = conn_bd.busca_relatorio(where='id', value=relatorio_id)
    return results

@app.route('/feedback/<nusp_aluno>', methods=['POST'])
def get_detalhes_aluno(nusp_aluno):
    detalhes_aluno = conn_bd.busca_detalhes_aluno(nusp_aluno)
    
    if detalhes_aluno:
        return render_template('feedback.html', nusp_aluno=nusp_aluno)
    else:
        return "Aluno não encontrado", 404



if __name__ == '__main__':
    app.run(debug=True)