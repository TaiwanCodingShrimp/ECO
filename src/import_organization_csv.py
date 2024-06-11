from random import randint

import pandas as pd

from Organization.models import WelfareOrganization


class create_organization:
    def random_with_N_digits(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10**n) - 1
        return randint(range_start, range_end)

    def run(self):
        # 讀取 CSV 文件
        csv_file_path = "src/res/welfare_organization_data.csv"
        df = pd.read_csv(csv_file_path, nrows=50)

        # 將數據插入到數據庫中
        welfare_agencies = []

        for index, row in df.iterrows():
            address = row["address"]
            county = address[:3]  # 解析 address 欄位的前三碼
            district = address[3:6]  # 解析 address 欄位的第4到第6個字
            fake_phone = str(self.random_with_N_digits(8))
            welfare_agencies.append(
                WelfareOrganization(
                    name=row["name"],
                    county=county,
                    district=district,
                    phone="09" + fake_phone,
                    address=address,
                )
            )

        WelfareOrganization.objects.bulk_create(welfare_agencies, batch_size=500)

        print("Data imported successfully!")
