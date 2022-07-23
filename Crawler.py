#Bibliotecas utilizadas
import requests
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
import collections

#Url a ser extraído e identificador
url = 'https://www.reclameaqui.com.br/empresa/claro/lista-reclamacoes/'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

#nltk.download('stopwords') É necessário realizar o download do pacote em português
stopword = nltk.corpus.stopwords.words('portuguese')

def nuvem(text):
  text = text.split()
  c = collections.Counter(text)
  lista = []
  for x in c:
    if x not in stopword:
      lista.append(x)
    else:
      pass
  nuvem_c = collections.Counter(lista).most_common(15)
  return [x[0] for x in nuvem_c]

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

for i in range(1, 2):
    url_pag = f"https://www.reclameaqui.com.br/empresa/claro/lista-reclamacoes/?pagina={i}"
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    reclamacoes = soup.find_all('div', class_=re.compile('bJdtis'))

    for classe in reclamacoes:

        link = classe.find('a')['href']
        url_href = f"https://www.reclameaqui.com.br{link}"
        rec = {'reclamação': url_href}


        def topicos():
            tag = []
            for _ in sopa.find_all('div', class_='eYkobe'):
                x = _.get_text().strip()
                tag.append(x)
            return list(set(tag))

        for value in rec.values():
            site2 = requests.get(value, headers=headers)
            sopa = BeautifulSoup(site2.content, 'html.parser')
            tags = topicos()
            titulo = sopa.find('h1', class_=re.compile('berwWw')).get_text().strip()
            texto = sopa.find('p', class_=re.compile('fXwQIB')).get_text().strip()
            texto_c = nuvem(texto)
            print("titulo: ",titulo)
            print("tags: ",tags)
            print("resumo: ",texto_c)
            print("link: ", url_href)
            print(" ")

