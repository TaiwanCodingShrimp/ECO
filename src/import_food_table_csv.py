import pandas as pd

from Users.models.datas import Food_Table


class create_food_Table:
    def run(self):
        csv_file_path = "src/res/food_carbon_data.csv"
        df = pd.read_csv(csv_file_path, nrows=50)

        food_agencies = []

        for index, row in df.iterrows():
            food_agencies.append(
                Food_Table(
                    item=row["item"],
                    carbon_footprint=row["carbon_footprint"],
                )
            )

        Food_Table.objects.bulk_create(food_agencies, batch_size=500)

        print("Data imported successfully!")
