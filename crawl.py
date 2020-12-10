from bs4 import BeautifulSoup
from tqdm import tqdm

pmidlist = []
with open ("pmid-nationalhe-set.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        pmidlist.append(line.strip('\n'))
pubmed_ids = pmidlist
abstracts = []

for id in tqdm(pubmed_ids): 
    html_for_id = requests.get('http://www.ncbi.nlm.nih.gov/pubmed/{0}'.format(id))
    soup =  BeautifulSoup(html_for_id.text,'xml')
    try:
        abstract = soup.find(id = 'enc-abstract').text
        abstract = abstract.strip()
        abstract = abstract.replace("\'" , "'" )
    except AttributeError:
        abstracts.append("None")
    
    abstracts.append(abstract)