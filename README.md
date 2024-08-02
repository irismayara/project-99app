# Projeto de Extração de Dados de Recibos do 99App

Este projeto tem como objetivo extrair informações específicas de recibos HTML gerados pelo 99App e armazená-las em um arquivo CSV.

## Funcionalidades

- Extrair dados de recibos HTML, incluindo:
  - Data
  - Método de Pagamento
  - Distância
  - Duração
  - Tipo de Corrida
  - Placa do Veículo
  - Nome do Motorista
  - Hora de Início
  - Local de Início
  - Hora de Chegada
  - Local de Chegada
  - Valor da Corrida
- Armazenar os dados extraídos em um arquivo CSV.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - beautifulsoup4
  - pandas
  - os

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/irismayara/project-99app.git
    cd project-99app
    ```

2. Instale os pacotes requeridos:

    ```sh
    pip install -r requirements.txt
    ```

## Utilização

1. Coloque os arquivos HTML dos recibos na pasta `recibos`.

2. Execute o script de extração de dados:

    ```sh
    python extract_data.py
    ```

3. Os dados extraídos serão salvos em um arquivo CSV chamado `recibos.csv`.
