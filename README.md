## Descrição

Este projeto foi desenvolvido para realizar o scraping de dados de sites específicos, processar os dados e carregá-los no Google BigQuery. O projeto utiliza diversas utilidades para manipulação de dados, como o processamento de arquivos Excel, o carregamento de arquivos CSV para o BigQuery e a execução de scripts SQL. Além disso, inclui funcionalidade para fazer scraping de arquivos de páginas web e salvá-los localmente.

## Funcionalidades

- **Web Scraping**: Realiza scraping de páginas web para encontrar links de download e salvar os arquivos localmente.
- **Processamento de Dados**: Processa arquivos Excel para extrair e limpar os dados, e depois os salva como CSV.
- **Integração com BigQuery**: Carrega arquivos CSV processados no Google BigQuery para análise posterior.
- **Execução de SQL**: Executa scripts SQL no BigQuery para refinar e manipular os dados.

## Requisitos

- Python 3.10+
- Google Cloud SDK para BigQuery (`google-cloud-bigquery`)
- BeautifulSoup (`beautifulsoup4`)
- Requests (`requests`)
- Pandas (`pandas`)

Você pode instalar os pacotes Python necessários com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Estrutura de Diretórios

```bash
projeto/
│
├── src/
│   ├── utils/
│   │   ├── processing.py      # Funções para processar dados ICC e ICF
│   │   ├── scrapper.py        # Utilitário de web scraping
│   │   └── big_query.py       # Funções para carregar dados no BigQuery
│   └── main.py                # Script principal para orquestrar o fluxo de trabalho
│
├── test/                      # Testes unitários do projeto
│   └── test_functions.py      # Testes para scraping, processamento de dados e funções do BigQuery
│
├── data/                      # Pasta para armazenar dados raspados e arquivos processados
│   ├── raw/
│   └── processed/
│
├── credentials/               # Diretório para as credenciais do Google Cloud (deve ser excluído do Git)
│
├── sql/                       # Scripts SQL para refinamento de dados
│   ├── trusted.sql
│   └── icf_icc_refined.sql
│
├── .gitignore                 # Arquivo gitignore para excluir arquivos desnecessários
├── requirements.txt           # Dependências do Python
└── README.md                  # Descrição do projeto e instruções de configuração
```

## Instruções de Configuração
### Clone o repositório:

```bash
git clone https://github.com/Tfcosendey/ds3x_test.git
cd ds3x_test
```
### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Configure suas credenciais do Google Cloud. Certifique-se de que a pasta credentials/ contenha o arquivo JSON apropriado para autenticação.

### Execute o projeto:
```bash
python src/main.py
```

## Testes
### Para executar os testes do projeto, use o seguinte comando:
```bash
pytest test/test_functions.py
```
