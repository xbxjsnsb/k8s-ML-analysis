import requests as requests
import csv
from datetime import datetime

url = 'http:// /api/v1/query_range'

params = {
    'query': 'sum(rate(container_cpu_usage_seconds_total{container_name!="POD",pod_name!="hello-minikube"}[5m]))',
    'start': '1611187200',
    'end'  : '1611273600',
    'step' : '30s'
}


response = requests.get(url, params = params)

rawdata = response.json()['data']['result'][0]['values']


with open('data1.csv', 'w') as file:
    writer = csv.writer(file)
    for measurment in rawdata:
        writer.writerow([datetime.utcfromtimestamp(measurment[0]).strftime('%Y-%m-%d %H:%M:%S'), measurment[1]])