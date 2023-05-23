import requests
from bs4 import BeautifulSoup

# Make a GET request to the web page
url = 'https://www.example.com/index.html'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the divs containing the data you want to extract
imoveis_venda_div = soup.find('div', {'id': 'imoveis-venda'})
imoveis_aluguel_div = soup.find('div', {'id': 'imoveis-aluguel'})

# Extract the data from the divs
imoveis_venda = []
for div in imoveis_venda_div.find_all('div', {'class': 'imovel'}):
    endereco = div.find('div', {'class': 'endereco'}).text.strip()
    preco = div.find('div', {'class': 'preco'}).text.strip()
    tamanho = div.find('div', {'class': 'tamanho'}).text.strip()
    quartos = div.find('div', {'class': 'quartos'}).text.strip()
    imovel = {'endereco': endereco, 'preco': preco, 'tamanho': tamanho, 'quartos': quartos}
    imoveis_venda.append(imovel)

imoveis_aluguel = []
for div in imoveis_aluguel_div.find_all('div', {'class': 'imovel'}):
    endereco = div.find('div', {'class': 'endereco'}).text.strip()
    preco = div.find('div', {'class': 'preco'}).text.strip()
    tamanho = div.find('div', {'class': 'tamanho'}).text.strip()
    quartos = div.find('div', {'class': 'quartos'}).text.strip()
    imovel = {'endereco': endereco, 'preco': preco, 'tamanho': tamanho, 'quartos': quartos}
    imoveis_aluguel.append(imovel)

# Print the extracted data
print('Imóveis à venda:')
for imovel in imoveis_venda:
    print(imovel)

print('Imóveis para alugar:')
for imovel in imoveis_aluguel:
    print(imovel)