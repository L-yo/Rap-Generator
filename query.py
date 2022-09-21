from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

f = open("french_rapper.sparql", "r")
sparql.setQuery(f.read())
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

df = pd.DataFrame(columns=['uri', 'name'])
d = []

for rapper in results['results']['bindings']:
    d.append(
        {
            'uri': rapper['rapper']['value'],
            'name': rapper['name']['value']
        }
    )

df = pd.DataFrame(d)
print(df.head(10))

df.to_csv('french_rappers.csv', index=False)