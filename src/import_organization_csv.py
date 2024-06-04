import os
import django
import pandas as pd

# 設置 Django 環境
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
#django.setup()

from Organization.models import WelfareOrganization

# 讀取 CSV 文件
csv_file_path = 'res/welfare_organization_data.csv'
df = pd.read_csv(csv_file_path, nrows = 50)

# 將數據插入到數據庫中
welfare_agencies = []

for index, row in df.iterrows():
    address = row['address']
    country = address[:3]  # 解析 address 欄位的前三碼
    district = address[3:6]  # 解析 address 欄位的第4到第6個字

    welfare_agencies.append(
        WelfareOrganization(
            name=row['name'],
            country=country,
            district=district,
            type='default_type'  #先設為default
        )
    )

WelfareOrganization.objects.bulk_create(welfare_agencies)

print("Data imported successfully!")
