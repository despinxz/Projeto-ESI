-- Active: 1733532974788@@127.0.0.1@5432@posgraduacao
CREATE TYPE nota AS ENUM ('Aguardando', 'Adequado', 'Adequado com ressalvas', 'Insatisfatório');
CREATE TYPE status_aluno AS ENUM ('Ativo', 'Inativo');

CREATE TABLE ccp (
  nusp INT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  senha VARCHAR(256) NOT NULL
);

CREATE TABLE professores (
  nusp INT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  senha VARCHAR(256) NOT NULL
);

CREATE TABLE alunos (
  nusp INT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(50) NOT NULL,
  senha VARCHAR(256) NOT NULL,
  data_nasc DATE NOT NULL,
  rg CHAR(10) UNIQUE,
  local_nasc VARCHAR(20) NOT NULL,
  nacionalidade VARCHAR(20) NOT NULL,
  lattes VARCHAR(50) NOT NULL,
  status_aluno status_aluno
);

CREATE TABLE cursos (
  nome VARCHAR(50) NOT NULL,
  id SERIAL PRIMARY KEY,
  aluno INT NOT NULL,
  orientador INT NOT NULL,
  data_matricula DATE NOT NULL,
  data_aprov_exam_qual DATE NOT NULL,
  data_aprov_exam_prof DATE NOT NULL,
  data_limite DATE NOT NULL,
  
  FOREIGN KEY (aluno)REFERENCES alunos(nusp),
  FOREIGN KEY (orientador) REFERENCES professores(nusp)
);

CREATE TABLE disciplinas (
  id INT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL
);

CREATE TABLE cursos_disciplinas_aprovadas (
  id_curso INT NOT NULL,
  id_disciplina INT NOT NULL,
  PRIMARY KEY (id_curso, id_disciplina),

  FOREIGN KEY (id_curso) REFERENCES cursos(id),
  FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id)
);

CREATE TABLE cursos_disciplinas_reprovadas (
  id_curso INT NOT NULL,
  id_disciplina INT NOT NULL,

  PRIMARY KEY (id_curso, id_disciplina),

  FOREIGN KEY (id_curso) REFERENCES cursos(id),
  FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id)
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

CREATE TABLE data_entrega_relatorio (
  id SERIAL PRIMARY KEY,
  data_entrega_relatorio DATE NOT NULL
);