from bs4 import BeautifulSoup
import pandas as pd
import os

def extract_data_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        data = []
        spans = soup.find_all('span')

        if('taxa de espera' in spans[3].get_text(strip=True)):
            for index, span in enumerate(spans):
                text = span.get_text(strip=True)

                if index not in (1, 2, 3, 5, 6, 15, 16, 17, 18, 19, 20, 21):
                    if(index == 7):
                        values = text.split('|')
                        for value in values:
                            data.append(value.strip())
                    else:
                        data.append(text)
        else:
            for index, span in enumerate(spans):
                text = span.get_text(strip=True)

                if index not in (1, 2, 4, 5, 14, 15, 16, 17, 18, 19, 20):
                    if(index == 6):
                        values = text.split('|')
                        for value in values:
                            data.append(value.strip())
                    else:
                        data.append(text)

        rows = soup.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 1:
                cell_text = cells[0].get_text(strip=True)
                if cell_text == 'Total':
                    data.append(cells[1].get_text(strip=True))
                if cell_text == 'Taxa de espera':
                    data.append(cells[1].get_text(strip=True))   

        return data

recibos_dir = r'C:\Users\iris.nunes\Documents\workspace-python\project-99app\recidos'
csv_output_file = 'recibos.csv'

all_data = []
for filename in os.listdir(recibos_dir):
    if filename.endswith('.html'):
        file_path = os.path.join(recibos_dir, filename)
        file_data = extract_data_from_html(file_path)
        if file_data:  
            all_data.append(file_data)  


df = pd.DataFrame(all_data, columns=[
    'DATA', 'METODO DE PAGAMENTO', 'DISTANCIA', 'DURACAO',
    'TIPO DE CORRIDA', 'PLACA DO VEICULO', 'MOTORISTA', 'HORA DE PARTIDA',
    'LOCAL DE PARTIDA', 'HORA DE CHEGADA', 'LOCAL DE CHEGADA', 'VALOR DA CORRIDA', 'TAXA DE ESPERA'
])

df.to_csv(csv_output_file, index=True)