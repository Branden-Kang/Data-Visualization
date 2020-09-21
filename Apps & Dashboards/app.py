import pandas as pd
from elasticsearch import Elasticsearch

# Database loading and service openning
database=pd.read_excel("data/test_db.xlsx")
es_client = Elasticsearch(http_compress=True)

#Elasticsearch does not accept NAN values
print(database.isna().sum().sum())

df=database.copy()
INDEX="laposte" #Its name in Elasticsearch (laposte for example)
TYPE= "record"

def rec_to_actions(df):
    import json
    for record in df.to_dict(orient="records"):
        yield ('{ "index" : { "_index" : "%s", "_type" : "%s" }}'% (INDEX, TYPE))
        yield (json.dumps(record, default=int))

e = Elasticsearch() 
r = e.bulk(rec_to_actions(df))

#Verify if everything went fine
print(not r["errors"])
