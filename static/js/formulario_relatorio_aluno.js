const nusp = "{{ nusp }}";
const url = "{{ url_for('aluno.index', nusp='') }}" + nusp

function enviarRelatorio(event) {
    event.preventDefault();

    const atividades_resp = document.getElementById('atividades_resp').value.trim();
    const pesquisas_resp = document.getElementById('pesquisas_resp').value.trim();
    const observacoes_resp = document.getElementById('obsercacoes_resp').value.trim();
    const dificuldade = document.querySelector('input[name="dificuldade"]:checked') ? 
                       document.querySelector('input[name="dificuldade"]:checked').id : null;
    const escrita = document.querySelector('input[name="escrita"]:checked');
    const aval = document.querySelector('input[name="aval"]:checked');
    const publicados = document.querySelector('input[name="publicados"]:checked');

    if (!atividades_resp || !pesquisas_resp || !observacoes_resp || !dificuldade || !escrita || !aval || !publicados){
        alert('Por favor, preencha todas as informações.');
        return;
    }
    
    const dadosRelatorio = {
        nusp,
        atividades_resp,
        pesquisas_resp,
        observacoes_resp,
        dificuldade,
        escrita: escrita.id,
        aval: aval.id,
        publicados: publicados.id
    };

    fetch(`/novo_relatorio/${nusp}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosRelatorio)
    })
    .then(response => {
        if (response.ok) {
            alert('Relatório enviado com sucesso!');
            window.location.href = url; 
        } else {
            throw new Error('Erro ao enviar relatório');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao enviar o relatório. Tente novamente.');
    });
}

document.querySelector('button').addEventListener('click', enviarRelatorio);
