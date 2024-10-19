-- Active: 1729174393765@@127.0.0.1@5432@posgraduacao@public

-- Inserir orientadores
INSERT INTO professores (nusp, nome) VALUES (1, 'Dr. Silva');
INSERT INTO professores (nusp, nome) VALUES (2, 'Dr. Souza');

-- Inserir alunos
INSERT INTO alunos (nusp, nome) VALUES (123456, 'Carlos');
INSERT INTO alunos (nusp, nome) VALUES (789101, 'Ana');
INSERT INTO alunos (nusp, nome) VALUES (654321, 'João');
INSERT INTO alunos (nusp, nome) VALUES (112233, 'Maria');
INSERT INTO alunos (nusp, nome) VALUES (445566, 'Pedro');


-- Inserir relatórios
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp,  aluno, orientador) 
VALUES ('Relatório teste 1', 'Texto para o primeiro relatório de teste.', '2022-10-10 11:30:30', 'Aguardando', 'Aguardando', 'Parecer ainda não enviado.', 'Parecer ainda não enviado.', 123456, 1);
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp,  aluno, orientador) 
VALUES ('Relatório teste 2', 'Texto para o segundo relatório de teste.', '2022-11-11 11:30:30', 'Adequado', 'Aguardando', 'Relatório 2 está adequado.', 'Parecer ainda não enviado.', 123456, 1);
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
VALUES ('Relatório teste 3', 'Texto para o terceiro relatório de teste.', '2022-12-12 11:30:30', 'Adequado com ressalvas', 'Aguardando', 'Relatório 3 tem algumas ressalvas.', 'Parecer ainda não enviado.', 123456, 1);
-- Inserir relatórios para Ana (já inserida)
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
VALUES ('Relatório teste 4', 'Texto para o quarto relatório de teste.', '2023-01-01 10:00:00', 'Insatisfatório', 'Aguardando', 'Relatório 4 está insatisfatório.', 'Parecer ainda não enviado.', 789101, 1);
-- Inserir relatórios para João
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
VALUES ('Relatório teste 5', 'Texto para o quinto relatório de teste.', '2023-02-15 09:45:00', 'Aguardando', 'Aguardando', 'Parecer ainda não enviado.', 'Parecer ainda não enviado.', 654321, 1);
-- Inserir relatórios para Maria
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
VALUES ('Relatório teste 6', 'Texto para o sexto relatório de teste.', '2023-03-20 12:20:00', 'Adequado', 'Adequado', 'Relatório 6 está adequado.', 'Parecer CCP adequado.', 112233, 1);
-- Inserir relatórios para Pedro
INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
VALUES ('Relatório teste 7', 'Texto para o sétimo relatório de teste.', '2023-04-25 14:00:00', 'Adequado com ressalvas', 'Adequado com ressalvas', 'Relatório 7 tem algumas ressalvas.', 'Parecer CCP com ressalvas.', 445566, 1);