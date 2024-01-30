import requests

csv_name = 'yellow_tripdata_2021-04.csv.gz'
csv_url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/{csv_name}'

response = requests.get(csv_url)

with open(csv_name, 'wb') as f:
    f.write(response.content)
