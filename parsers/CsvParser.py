import json
import xmltodict, json, csv
import pandas as pd

class CsvParser:

    def __init__(self, urls):
        self.urls = urls



    def to_json(self):
        customers = pd.read_csv(self.urls[0])
        vehicles = pd.read_csv(self.urls[1])
        for _ , row in customers.iterrows():
            transaction = {}
            data = {}
            data['file_name'] = self.urls[0]
            transaction['date'] = row['date']
            transaction['customer'] = row[['id','name','address','phone']].to_dict()
            transaction['vehicles'] = (vehicles[vehicles['owner_id'] == row['id']]).to_dict('records')
            data['transaction'] = transaction


            with open(f'output/output-{row["id"]}.json', "w+") as jsonfile:
                    jsonfile.write(json.dumps(data))
