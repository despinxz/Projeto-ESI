
# Website para Gestão de Relatórios da Pós-Graduação

## Descrição
Este projeto implementa um website que gerencia o envio de relatórios e notas do programa de pós-graduação.

## Instalação
Para configurar o ambiente e instalar as dependências necessárias, execute:
```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Este projeto utiliza PostgreSQL como banco de dados. Siga os passos abaixo para configurar o ambiente:

### 1. Pré-requisitos
- PostgreSQL instalado: [Download PostgreSQL](https://www.postgresql.org/download/).

### 2. Criar um banco de dados
Execute o comando no terminal:

```bash
createdb posgraduacao
```

### 3. Restaurar o dump do banco

Utilize os arquivos fornecidos no diretório \static\bd para a criação e população do banco de dados.

### 4. Configurar variáveis de ambiente

No arquivo .env do projeto, configure os dados de conexão.

## Uso

Para iniciar o servidor, execute o comando:

```bash
python app.py
```
