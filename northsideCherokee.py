import pandas as pd
import csv
import json
import requests

url = "https://api.hospitalpriceindex.com/itemList/list"

payload = "{\"defId\":8149,\"priceStatus\":\"published\",\"page\":{\"from\":1,\"size\":50000},\"sortInput\":[{\"reverse\":false,\"by\":\"description\"}],\"listName\":\"priceList\",\"filters\":[{\"property\":\"description\",\"value\":\"\",\"type\":\"all\"}]}"
headers = {
    'authority': 'api.hospitalpriceindex.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://search.hospitalpriceindex.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.hospitalpriceindex.com/',
    'accept-language': 'en-US,en;q=0.9'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# response_text = response.text

#
northsideData = response.json()
df = pd.json_normalize(northsideData['result'], record_path=['items'])
# df.transpose
json_data_path = 'C:\\Users\\jackb\\Desktop\\FileOpen\\geraldChampionRegionalMC\\northside\\northsideCherokee.json'
csv_write = r'C:\\Users\\jackb\\Desktop\\FileOpen\\northside\\northsideCherokee.csv'
df.to_csv(csv_write, index=False)

json_data_path = 'C:\\Users\\jackb\\Desktop\\FileOpen\\geraldChampionRegionalMC\\northside\\northsideCherokee.json'
csv_write = r'C:\\Users\\jackb\\Desktop\\FileOpen\\northside\\northsideCherokee.csv'

# json_data.to_csv(csv_write, index=False)
# print(json_data.head)
