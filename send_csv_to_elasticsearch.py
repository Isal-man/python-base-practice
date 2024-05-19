from elasticsearch import Elasticsearch
import csv

# URL elasticsearch
elk_url = "https://192.168.10.253:9200/"

# Username and password
username = 'elastic'
password = 'P@ssw0rd123'

# File CA certificate
ca_path = "faisal-elk.crt"

# Menambahkan autentikasi dan SSL
client = Elasticsearch(
    hosts=[elk_url],
    basic_auth=(username, password),
    verify_certs=False
)

# Nama indeks dan tipe dokumen di Elasticsearch
index_name = 'credit_card_index'
doc_type = 'csv'

try:
    # Membaca file CSV
    with open('Credit Card Dashboard.csv', 'r', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Mengirimkan setiap baris data ke Elasticsearch
        for row in reader:
            response = client.index(index=index_name, body=row)
            print(response)  # Optional: print response for each indexed document
except Exception as e:
    print(f"An error occurred: {e}")