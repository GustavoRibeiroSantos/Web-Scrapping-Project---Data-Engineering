# Projeto de Extração Automática e Armazenamento de Dados

Este é o meu primeiro projeto de Data Engineering, onde desenvolvi uma aplicação em Python para extrair dados de várias páginas da web de forma automática e agendada. Os dados extraídos são então armazenados em um banco de dados local.

## Descrição

Este projeto foi criado como parte da minha jornada de aprendizado em Data Engineering. Ele demonstra a automação da extração de dados de fontes web e a armazenagem desses dados em um banco de dados para análise posterior.

## Funcionalidades

- [x] API criada em Django
- [x] Extração de dados de páginas web utilizando bibliotecas como Beautiful Soup e Selenium
- [x] Agendamento automático das tarefas de extração usando uma ferramenta como o Cron
- [x] Armazenamento dos dados em um banco de dados local Postgresql
- [x] Gerenciamento de erros e retentativas para garantir a confiabilidade da extração

## Estrutura do Projeto

- `BookClub/`: Contém o código-fonte da aplicação de extração
- `static/`: Armazena o chromedriver
- `first_project_data_engineering/`: Contém os arquivos de configuração do Django

## Como Usar

1. Clone este repositório em sua máquina local.
2. Navegue até o diretório do projeto.
3. Configure as páginas da web que você deseja extrair no código-fonte.
4. Instale as dependências usadas.
5. Configure o agendamento das tarefas de extração usando ferramentas como o Cron.
6. Execute o script de extração para começar a coletar dados.

```bash
git clone https://github.com/GustavoRibeiroSantos/First-Data-analytics-project.git
cd First-Data-analytics-project
python manage.py
```

## Contribuição
Contribuições são bem-vindas! Se você encontrar problemas, bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir problemas ou enviar pull requests.

### Divirta-se explorando e processando os dados! 📊🔍
