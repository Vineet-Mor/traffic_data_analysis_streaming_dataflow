from google.cloud import bigquery
client = bigquery.Client(project="quixotic-treat-419302")
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US" 
dataset_id=f"quixotic-treat-419302.traffic_data"
dataset = bigquery.Dataset(dataset_id)
dataset = client.create_dataset(dataset, timeout=30) 

print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

schema = [ bigquery.SchemaField("item_id", "INTEGER", mode="REQUIRED"), bigquery.SchemaField("product", "STRING", mode="REQUIRED"), bigquery.SchemaField("price", "INTEGER", mode="REQUIRED"), ]

table_id = dataset_id+f".sales_2024_{month}_{date}"
table = bigquery.Table(table_id, schema=schema) 
table = client.create_table(table)

#bq mk traffic_data
#bq mk --table traffic_data.average_speed schema.json
