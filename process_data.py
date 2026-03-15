import pandas as pd

df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

#combining them into one dataset
df = pd.concat([df1, df2, df3])

#keeping only pink morsel
df = df[df["product"] == "pink morsel"]

#converting price to numeric
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

#calculating sales
df["sales"] = df["quantity"] * df["price"]

#required columns
output = df[["sales", "date", "region"]]

#save to csv
output.to_csv('formatted_sales_data.csv', index=False)

print("Data processing complete. File Saved as formatted_sales_data.csv")