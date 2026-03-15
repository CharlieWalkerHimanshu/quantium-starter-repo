import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        id="header",
        className="header"
    ),

    html.Div([
        html.Label("Select Region:", className="label"),

        dcc.RadioItems(
            id="region-picker",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            className="radio"
        )
    ], className="filter-container"),

    dcc.Graph(id="sales-chart")

], className="container")


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    sales_by_date = (
        filtered_df.groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        }
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)