INSERT INTO professores (nusp, nome, senha) VALUES (1, 'Dr. Silva', 'senha123');
INSERT INTO professores (nusp, nome, senha) VALUES (2, 'Dr. Souza', 'senha123');

INSERT INTO alunos (nusp, nome, email, senha, data_nasc, rg, local_nasc, nacionalidade, lattes, status_aluno) 
VALUES (123456, 'Carlos', 'carlos@dominio.com', 'senha123', '1995-06-12', '123456789', 'São Paulo', 'Brasileiro', 'http://lattes.carlos.com', 'Ativo');
INSERT INTO alunos (nusp, nome, email, senha, data_nasc, rg, local_nasc, nacionalidade, lattes, status_aluno) 
VALUES (789101, 'Ana', 'ana@dominio.com', 'senha123', '1996-07-23', '987654321', 'Rio de Janeiro', 'Brasileira', 'http://lattes.ana.com', 'Ativo');
INSERT INTO alunos (nusp, nome, email, senha, data_nasc, rg, local_nasc, nacionalidade, lattes, status_aluno) 
VALUES (654321, 'João', 'joao@dominio.com', 'senha123', '1994-04-10', '123789456', 'Belo Horizonte', 'Brasileiro', 'http://lattes.joao.com', 'Ativo');
INSERT INTO alunos (nusp, nome, email, senha, data_nasc, rg, local_nasc, nacionalidade, lattes, status_aluno) 
VALUES (112233, 'Maria', 'maria@dominio.com', 'senha123', '1997-08-19', '456123789', 'Curitiba', 'Brasileira', 'http://lattes.maria.com', 'Inativo');
INSERT INTO alunos (nusp, nome, email, senha, data_nasc, rg, local_nasc, nacionalidade, lattes, status_aluno) 
VALUES (445566, 'Pedro', 'pedro@dominio.com', 'senha123', '1995-12-25', '321654987', 'São Paulo', 'Brasileiro', 'http://lattes.pedro.com', 'Inativo');

INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 1', 'Texto para o primeiro relatório de teste.', 'Pesquisas realizadas pelo aluno.', 'Observações do relatório.', 'Sim', '2022-10-10 11:30:30', 'Aguardando', 'Aguardando', 'Parecer ainda não enviado.', 'Parecer ainda não enviado.', 123456, 1, 'S', 'S', 'S');
INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 2', 'Texto para o segundo relatório de teste.', 'Pesquisas realizadas por Ana.', 'Observações do relatório.', 'Sim', '2022-11-11 11:30:30', 'Adequado', 'Aguardando', 'Relatório 2 está adequado.', 'Parecer ainda não enviado.', 123456, 1, 'S', 'S', 'S');
INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 3', 'Texto para o terceiro relatório de teste.', 'Pesquisas realizadas por João.', 'Observações do relatório.', 'Não', '2022-12-12 11:30:30', 'Adequado com ressalvas', 'Aguardando', 'Relatório 3 tem algumas ressalvas.', 'Parecer ainda não enviado.', 654321, 1, 'S', 'S', 'S');
INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 4', 'Texto para o quarto relatório de teste.', 'Pesquisas realizadas por Maria.', 'Observações do relatório.', 'Sim', '2023-01-01 10:00:00', 'Insatisfatório', 'Aguardando', 'Relatório 4 está insatisfatório.', 'Parecer ainda não enviado.', 789101, 1, 'S', 'S', 'S');
INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 5', 'Texto para o quinto relatório de teste.', 'Pesquisas realizadas por João.', 'Observações do relatório.', 'Não', '2023-02-15 09:45:00', 'Aguardando', 'Aguardando', 'Parecer ainda não enviado.', 'Parecer ainda não enviado.', 654321, 1, 'S', 'S', 'S');
INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 6', 'Texto para o sexto relatório de teste.', 'Pesquisas realizadas por Maria.', 'Observações do relatório.', 'Sim', '2023-03-20 12:20:00', 'Adequado', 'Adequado', 'Relatório 6 está adequado.', 'Parecer CCP adequado.', 112233, 1, 'S', 'S', 'S');
INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 7', 'Texto para o sétimo relatório de teste.', 'Pesquisas realizadas por Pedro.', 'Observações do relatório.', 'Sim', '2023-04-25 14:00:00', 'Adequado com ressalvas', 'Adequado com ressalvas', 'Relatório 7 tem algumas ressalvas.', 'Parecer CCP com ressalvas.', 445566, 1, 'S', 'S', 'S');

INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 8', 'Texto para o oitavo relatório de teste.', 'Pesquisas realizadas por Pedro.', 'Observações do relatório.', 'Sim', '2024-12-25 14:00:00', 'Adequado com ressalvas', 'Insatisfatório', 'Relatório 8 tem algumas ressalvas.', 'Parecer CCP insatisfatório.', 445566, 1, 'S', 'S', 'S');

INSERT INTO relatorios (titulo, atividades_resp, pesquisas_resp, observacoes_resp, dificuldade, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador, escrita, aval, publicados) 
VALUES ('Relatório teste 9', 'Texto para o nono relatório de teste.', 'Pesquisas realizadas por Pedro.', 'Observações do relatório.', 'Sim', '2024-12-24 14:00:00', 'Adequado com ressalvas', 'Insatisfatório', 'Relatório 9 tem algumas ressalvas.', 'Parecer CCP insatisfatório.', 445566, 1, 'S', 'S', 'S');

INSERT INTO data_entrega_relatorio (data_entrega_relatorio)
VALUES ('1995-06-12');

INSERT INTO cursos (nome, id, aluno, orientador, data_matricula, data_aprov_exam_qual, data_aprov_exam_prof, data_limite, ativo) VALUES ('Mestrado', 1, 445566, 2, '2024-06-12', '2024-01-12', '2024-01-01', '2025-06-12', true);
INSERT INTO cursos (nome, id, aluno, orientador, data_matricula, data_aprov_exam_qual, data_aprov_exam_prof, data_limite, ativo) VALUES ('Mestrado', 2, 112233, 2, '2024-06-12', '2024-01-12', '2024-01-01', '2025-06-12', true);
INSERT INTO cursos (nome, id, aluno, orientador, data_matricula, data_aprov_exam_qual, data_aprov_exam_prof, data_limite, ativo) VALUES ('Doutorado', 3, 654321, 2, '2024-06-12', '2024-01-12', '2024-01-01', '2025-06-12', true);
INSERT INTO cursos (nome, id, aluno, orientador, data_matricula, data_aprov_exam_qual, data_aprov_exam_prof, data_limite, ativo) VALUES ('Mestrado', 4, 789101, 2, '2021-06-12', '2021-01-12', '2021-01-01', '2023-12-01', false);
INSERT INTO cursos (nome, id, aluno, orientador, data_matricula, data_aprov_exam_qual, data_aprov_exam_prof, data_limite, ativo) VALUES ('Doutorado', 5, 789101, 2, '2024-06-12', '2024-01-12', '2024-01-01', '2025-06-12', true);
INSERT INTO cursos (nome, id, aluno, orientador, data_matricula, data_aprov_exam_qual, data_aprov_exam_prof, data_limite, ativo) VALUES ('Doutorado', 6, 123456, 2, '2024-06-12', '2024-01-12', '2024-01-01', '2025-06-12', true);