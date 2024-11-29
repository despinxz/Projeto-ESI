const nusp_aluno = "{{ nusp_aluno }}";  

    // Função para buscar os detalhes do aluno
    function fetchDetalhesAluno() {
        etch(`/feedback_ccp/${nusp_aluno}`)
        .then(response => response.json())
        .then(data => {
            const detalhes = data.detalhes_aluno[0];
            document.getElementById('nome_aluno').textContent = detalhes.nome;
            document.getElementById('nusp').textContent = detalhes.nusp;
            document.getElementById('data_envio').textContent = detalhes.data_envio;
            document.getElementById('curso').textContent = detalhes.curso;
            document.getElementById('link_lattes').textContent = detalhes.lattes;
            document.getElementById('aprovacoes').textContent = detalhes.aprovacoes;
            document.getElementById('reprovacoes').textContent = detalhes.reprovacoes;
            document.getElementById('parecer_professor').textContent = detalhes.parecer_professor;
            document.getElementById('ativ_acad').textContent = detalhes.atividades_academicas;
            document.getElementById('rem_pesquisa').textContent = detalhes.resumo_pesquisa;
        })
        .catch(error => console.error('Erro ao buscar dados do aluno:', error));
    }

    document.getElementById('enviar_parecer').addEventListener('click', () => {
        const parecer_resp = document.getElementById('parecer_resp').value;
        const nivel = document.querySelector('input[name="nivel"]:checked');

        if (!parecer_resp) {
            alert('Por favor, preencha o parecer.');
            return;
        }

        if (!nivel) {
            alert('Por favor, selecione um nível de desempenho.');
            return;
        }

        const nivelValue = nivel.value; // Aqui capturamos o valor do nível

        fetch(`/feedback_ccp/${nusp_aluno}/save`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                parecer_resp: parecer_resp,
                nivel: nivelValue // Envia o valor do nível
            })
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'Erro desconhecido.');
                });
            }
            return response.json();
        })
        .then(data => {
            if (data.sucesso) {
                alert(data.mensagem);
            } else {
                alert('Erro ao salvar o parecer: ' + (data.mensagem || 'Erro desconhecido.'));
            }
        })
        .catch(error => alert('Erro ao enviar parecer: ' + error.message));
    });

    // Chama a função para buscar os detalhes do aluno ao carregar a página
    fetchDetalhesAluno();