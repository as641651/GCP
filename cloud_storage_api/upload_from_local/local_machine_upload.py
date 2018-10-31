#pip install google-cloud-storage
from google.cloud import storage

#pass the service account key as credentials
client = storage.Client.from_service_account_json('test-engine-service.json')
bucket = client.get_bucket("senesence-bkt-1")
blob = bucket.blob("sql/new_from_aravind.txt")
blob.upload_from_filename("new.txt")
