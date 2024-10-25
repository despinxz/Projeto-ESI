-- Active: 1729174393765@@127.0.0.1@5432@posgraduacao@public

-- Inserir orientadores
INSERT INTO professores (nusp, nome) VALUES (1, 'Dr. Silva');
INSERT INTO professores (nusp, nome) VALUES (2, 'Dr. Souza');

-- Inserir alunos
INSERT INTO alunos (nusp, nome, email, data_nasc, rg, local_nasc, nacionalidade, lattes) VALUES 
(101, 'Ana Silva', 'ana.silva@email.com', '1992-05-14', '1234567890', 'São Paulo', 'Brasileira', 'http://lattes.cnpq.br/ana_silva'),
(102, 'Carlos Souza', 'carlos.souza@email.com', '1990-09-20', '0987654321', 'Rio de Janeiro', 'Brasileiro', 'http://lattes.cnpq.br/carlos_souza'),
(103, 'Beatriz Oliveira', 'beatriz.oliveira@email.com', '1995-03-08', '1122334455', 'Belo Horizonte', 'Brasileira', 'http://lattes.cnpq.br/beatriz_oliveira'),
(104, 'Fernando Lima', 'fernando.lima@email.com', '1988-12-25', '2233445566', 'Curitiba', 'Brasileiro', 'http://lattes.cnpq.br/fernando_lima'),
(105, 'Daniela Pereira', 'daniela.pereira@email.com', '1993-06-15', '3344556677', 'Porto Alegre', 'Brasileira', 'http://lattes.cnpq.br/daniela_pereira')
;

-- Inserir relatórios
-- INSERT INTO relatorios (texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp,  aluno, orientador) 
-- VALUES ('Texto para o primeiro relatório de teste.', '2022-10-10 11:30:30', 'Aguardando', 'Aguardando', 'Parecer ainda não enviado.', 'Parecer ainda não enviado.', 123456, 1);
-- INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp,  aluno, orientador) 
-- VALUES ('Texto para o segundo relatório de teste.', '2022-11-11 11:30:30', 'Adequado', 'Aguardando', 'Relatório 2 está adequado.', 'Parecer ainda não enviado.', 123456, 1);
-- INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
-- VALUES ('Texto para o terceiro relatório de teste.', '2022-12-12 11:30:30', 'Adequado com ressalvas', 'Aguardando', 'Relatório 3 tem algumas ressalvas.', 'Parecer ainda não enviado.', 123456, 1);
-- -- Inserir relatórios para Ana (já inserida)
-- INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
-- VALUES ('Texto para o quarto relatório de teste.', '2023-01-01 10:00:00', 'Insatisfatório', 'Aguardando', 'Relatório 4 está insatisfatório.', 'Parecer ainda não enviado.', 789101, 1);
-- -- Inserir relatórios para João
-- INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
-- VALUES ('Texto para o quinto relatório de teste.', '2023-02-15 09:45:00', 'Aguardando', 'Aguardando', 'Parecer ainda não enviado.', 'Parecer ainda não enviado.', 654321, 1);
-- -- Inserir relatórios para Maria
-- INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
-- VALUES ('Texto para o sexto relatório de teste.', '2023-03-20 12:20:00', 'Adequado', 'Adequado', 'Relatório 6 está adequado.', 'Parecer CCP adequado.', 112233, 1);
-- -- Inserir relatórios para Pedro
-- INSERT INTO relatorios (titulo, texto, data_envio, nota_professor, nota_ccp, parecer_professor, parecer_ccp, aluno, orientador) 
-- VALUES ('Texto para o sétimo relatório de teste.', '2023-04-25 14:00:00', 'Adequado com ressalvas', 'Adequado com ressalvas', 'Relatório 7 tem algumas ressalvas.', 'Parecer CCP com ressalvas.', 445566, 1);