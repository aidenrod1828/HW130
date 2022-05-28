import pandas as pd
import csv

df=pd.read_csv("scrapper_2.csv")
df.columns
df.remove("Luminosity")
df.remove("Unnamed:0", "Unnamed:6", "Star_name.1", "Distance", "Mass", "Radius")

with open("data_cleaning.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(df)