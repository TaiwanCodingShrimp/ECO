import pandas as pd

from Users.models.datas import FoodTable


class create_food_Table:
    def run(self):
        csv_file_path = "src/res/food_carbon_data.csv"
        df = pd.read_csv(csv_file_path, nrows=50)

        food_agencies = []

        for index, row in df.iterrows():
            food_agencies.append(
                FoodTable(
                    item=row["item"],
                    carbon_factor=row["carbon_footprint"],
                )
            )

        FoodTable.objects.bulk_create(food_agencies, batch_size=500)

        print("Data imported successfully!")
