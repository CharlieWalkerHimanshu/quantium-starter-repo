import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

#load processed data
df = pd.read_csv('formatted_sales_data.csv')

#converting the date column to datatime
df["date"] = pd.to_datetime(df["date"])

#sort data by date
df = df.sort_values("date")

#aggregate sales by date
sales_by_date = df.groupby("date")["sales"].sum().reset_index()

#create line chart
fig = px.line(
    sales_by_date,
    x="date",
    y= "sales",
    title="Pink Moresel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales",
    }
)

#dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)