-- decidir como vai ser o UPDATE e o DELETE, cascade ou nao
CREATE TYPE nota AS ENUM ('Aguardando', 'Adequado', 'Adequado com ressalvas', 'Insatisfatório');

CREATE TABLE ccp (
  id INT PRIMARY KEY, 
  nome VARCHAR(100) NOT NULL
);

CREATE TABLE professores (
  nusp INT PRIMARY KEY, -- professor tem nusp?
  nome VARCHAR(100) NOT NULL
);

CREATE TABLE alunos (
  nusp INT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  curso VARCHAR(50) NOT NULL,
  lattes VARCHAR(500) NOT NULL,
  aprovacoes INT NOT NULL,
  reprovacoes INT NOT NULL
);

CREATE TABLE relatorios (
  id SERIAL PRIMARY KEY, 
  titulo VARCHAR(100) NOT NULL,
  texto VARCHAR(5000) NOT NULL, -- não sei o limite de caracteres
  data_envio TIMESTAMP,
  nota_professor nota,
  nota_ccp nota,
  parecer_professor VARCHAR(1000),
  parecer_ccp VARCHAR(1000),
  aluno INT NOT NULL,
  orientador INT NOT NULL,
  atividades_academicas VARCHAR(5000) NOT NULL,
  resumo_pesquisa VARCHAR(5000) NOT NULL,
  CONSTRAINT fk_aluno
    FOREIGN KEY (aluno)
    REFERENCES alunos(nusp),
  
  CONSTRAINT fk_orientador
    FOREIGN KEY (orientador) 
    REFERENCES professores(nusp)
);