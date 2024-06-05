import pandas as pd

from Organization.models import Food_Bank

df = pd.read_csv("src/res/food_bank_data.csv", encoding="utf-8")
print(df)
food_bank_list = []

for index, row in df.iterrows():
    food_bank_list.append(
        Food_Bank(
            id=row["id"],
            name=row["name"],
            county=row["county"],
            district=row["district"],
            address=row["address"],
            contact=row["contact"],
        )
    )
Food_Bank.objects.bulk_create(food_bank_list, batch_size=500)
print("Data imported successfully!")
