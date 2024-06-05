import csv

import pandas as pd

from Organization.models import Food_Bank

welfare_organizations = [
    {
        "id": 1,
        "name": "仁愛之家",
        "county": "台北市",
        "address": "台北市中正區和平東路123號",
        "contact": "02-12345678",
    },
    {
        "id": 2,
        "name": "和平之家",
        "county": "新北市",
        "address": "新北市板橋區文化路456號",
        "contact": "02-23456789",
    },
    {
        "id": 3,
        "name": "祥和之家",
        "county": "台中市",
        "address": "台中市西屯區台灣大道789號",
        "contact": "04-34567890",
    },
    {
        "id": 4,
        "name": "幸福之家",
        "county": "台南市",
        "address": "台南市安平區健康路101號",
        "contact": "06-45678901",
    },
    {
        "id": 5,
        "name": "友愛之家",
        "county": "高雄市",
        "address": "高雄市苓雅區成功路202號",
        "contact": "07-56789012",
    },
    {
        "id": 6,
        "name": "康樂之家",
        "county": "桃園市",
        "address": "桃園市中壢區幸福路303號",
        "contact": "03-67890123",
    },
    {
        "id": 7,
        "name": "仁義之家",
        "county": "新竹市",
        "address": "新竹市北區光明路404號",
        "contact": "03-78901234",
    },
    {
        "id": 8,
        "name": "安和之家",
        "county": "苗栗縣",
        "address": "苗栗縣頭份市民生路505號",
        "contact": "037-8901234",
    },
    {
        "id": 9,
        "name": "永康之家",
        "county": "彰化縣",
        "address": "彰化縣彰化市中正路606號",
        "contact": "04-90123456",
    },
    {
        "id": 10,
        "name": "德善之家",
        "county": "南投縣",
        "address": "南投縣草屯鎮山明路707號",
        "contact": "049-0123456",
    },
]

with open("src/res/food_bank_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file, fieldnames=["id", "name", "county", "address", "contact"]
    )
    writer.writeheader()
    writer.writerows(welfare_organizations)

df = pd.read_csv("src/res/food_bank_data.csv", encoding="utf-8")

for index, row in df.iterrows():
    Food_Bank.objects.bulk_create(
        id=row["id"],
        name=row["name"],
        county=row["county"],
        address=row["address"],
        contact=row["contact"],
    )
