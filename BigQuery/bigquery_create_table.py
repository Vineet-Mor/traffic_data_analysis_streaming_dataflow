from google.cloud import bigquery
client = bigquery.Client(project="quixotic-treat-419302")
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US" 
dataset_id=f"quixotic-treat-419302.traffic_data"
dataset = bigquery.Dataset(dataset_id)
dataset = client.create_dataset(dataset, timeout=30) 

print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

schema = [ bigquery.SchemaField(
  {"name": "timestamp", "type": "TIMESTAMP"},
  {"name": "speed", "type": "FLOAT"},
  {"name": "location", "type": "STRING"}
]

table_id = dataset_id+"traffic_data.average_speed"
table = bigquery.Table(table_id, schema=schema) 
table = client.create_table(table)

#bq mk traffic_data
#bq mk --table traffic_data.average_speed schema.json
