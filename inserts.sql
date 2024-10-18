-- Active: 1729174393765@@127.0.0.1@5432@posgraduacao@public

-- Inserir orientadores
INSERT INTO professores (nusp, nome) VALUES (1, 'Dr. Silva');
INSERT INTO professores (nusp, nome) VALUES (2, 'Dr. Souza');

-- Inserir alunos
INSERT INTO alunos (nusp, nome) VALUES (123456, 'Carlos');
INSERT INTO alunos (nusp, nome) VALUES (789101, 'Ana');

-- Inserir relatórios
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp,  aluno, orientador) VALUES ('Relatório teste 1', 'Texto para o primeiro relatório de teste.', '2022-10-10 11:30:30', 'Aguardando', 'Aguardando', 'Parecer ainda não enviado.', 'Parecer ainda não enviado.', 123456, 1);
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp,  aluno, orientador) VALUES ('Relatório teste 2', 'Texto para o segundo relatório de teste.', '2022-11-11 11:30:30', 'Adequado', 'Aguardando', 'Relatório 2 está adequado.', 'Parecer ainda não enviado.', 123456, 1);
