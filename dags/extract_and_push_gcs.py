import csv
import requests
from google.cloud import storage

url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'
headers = {
    'x-rapidapi-key': "cd70100bdfmshb71f854776f142cp175af5jsn16a08fca147b",
    'x-rapidapi-host': "cricbuzz-cricket.p.rapidapi.com"
}

params = {
    'formatType': 'odi'
}

response = requests.get(url, headers=headers, params=params)
print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json().get('rank', [])  # Extracting the 'rank' data
    csv_filename = 'batsmen_rankings.csv'

    if data:
        field_names = ['rank', 'name', 'country']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            # writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")

        # Upload CSV file to GCS
        bucket_name = 'airflow-cricbuzz-akhilproject1'
        storage_client = storage.Client(project="smart-mark-438604-n2")
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The path to store in GCS

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")

    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)