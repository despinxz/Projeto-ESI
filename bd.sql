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
  email VARCHAR(50) NOT NULL,
  data_nasc DATE NOT NULL,
  rg CHAR(10) UNIQUE,
  local_nasc VARCHAR(20) NOT NULL,
  nacionalidade VARCHAR(20) NOT NULL,
  lattes VARCHAR(50) NOT NULL
);


CREATE TABLE relatorios (
  id SERIAL PRIMARY KEY, 
  titulo VARCHAR(100) NOT NULL,
  atividades_resp VARCHAR(5000) NOT NULL, -- não sei o limite de caracteres
  pesquisas_resp VARCHAR(5000) NOT NULL,
  observacoes_resp VARCHAR(5000) NOT NULL,
  dificuldade CHAR(3) CHECK (dificuldade IN ('Sim', 'Não')),
  data_envio TIMESTAMP,
  nota_professor nota,
  nota_ccp nota,
  parecer_professor VARCHAR(1000),
  parecer_ccp VARCHAR(1000),
  aluno INT NOT NULL,
  orientador INT NOT NULL, 
  escrita CHAR(1) NOT NULL,
  aval CHAR(1) NOT NULL,
  publicados CHAR(1) NOT NULL,



  CONSTRAINT fk_aluno
    FOREIGN KEY (aluno)
    REFERENCES alunos(nusp),
  
  CONSTRAINT fk_orientador
    FOREIGN KEY (orientador) 
    REFERENCES professores(nusp)
);