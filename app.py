import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

total_sales = df["sales"].sum()
peak_day = df.groupby("date")["sales"].sum().idxmax().strftime("%b %d, %Y")
regions_count = df["region"].nunique()

app = dash.Dash(__name__)

app.layout = html.Div([

    # Top accent bar
    html.Div(className="accent-bar"),

    # Header
    html.Div([
        html.Div("✦  SOUL FOODS ANALYTICS  ✦", className="brand"),
        html.H1("Pink Morsel Sales Dashboard", id="header", className="header"),
        html.P("Real-time daily sales performance across all regions", className="subheader"),
    ], className="hero"),

    # Stat cards
    html.Div([
        html.Div([
            html.Span("💰", className="card-icon"),
            html.Div("Total Revenue", className="card-label"),
            html.Div(f"${total_sales:,.0f}", className="card-value"),
        ], className="stat-card"),
        html.Div([
            html.Span("📈", className="card-icon"),
            html.Div("Peak Sales Day", className="card-label"),
            html.Div(peak_day, className="card-value card-value--sm"),
        ], className="stat-card"),
        html.Div([
            html.Span("🌐", className="card-icon"),
            html.Div("Regions Tracked", className="card-label"),
            html.Div(str(regions_count), className="card-value"),
        ], className="stat-card"),
    ], className="stats-row"),

    # Filter + Chart
    html.Div([
        html.Div([
            html.Div([
                html.Div("Sales Over Time", className="chart-title"),
                html.Div("Aggregated daily pink morsel revenue", className="chart-subtitle"),
            ]),
            html.Div([
                html.Span("Regions:", className="label"),
                dcc.Checklist(
                    id="region-picker",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East",  "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West",  "value": "west"},
                    ],
                    value=["north", "east", "south", "west"],
                    inline=True,
                    className="radio",
                    inputClassName="radio-input",
                    labelClassName="radio-label"
                )
            ], className="filter-right"),
        ], className="filter-container"),

        dcc.Graph(id="sales-chart", className="chart", config={"displayModeBar": False})
    ], className="chart-section"),

    html.Div([
        html.Span("SOUL FOODS ANALYTICS"),
        html.Span(" · "),
        html.Span("Pink Morsel Division"),
    ], className="footer")

], className="page-wrap")


REGION_COLORS = {
    "north": "#e63946",
    "east":  "#f4a261",
    "south": "#2a9d8f",
    "west":  "#a78bfa",
}

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-picker", "value")
)
def update_chart(selected_regions):

    if not selected_regions:
        selected_regions = list(REGION_COLORS.keys())

    filtered_df = df[df["region"].isin(selected_regions)]

    sales_by_date = (
        filtered_df.groupby(["date", "region"])["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        color="region",
        title="",
        labels={"date": "", "sales": "", "region": "Region"},
        color_discrete_map=REGION_COLORS,
        custom_data=["region"]
    )

    fig.update_traces(
        line=dict(width=2.5),
        hovertemplate="<b>%{customdata[0].title()} · %{x|%b %d, %Y}</b><br>Revenue: <b>$%{y:,.0f}</b><extra></extra>"
    )

    fig.update_layout(
        paper_bgcolor="#0e0e16",
        plot_bgcolor="#0e0e16",
        font=dict(color="#94a3b8", family="Inter, Arial, sans-serif", size=12),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(color="#475569", size=11),
            tickformat="%b '%y",
            showline=True,
            linecolor="rgba(255,255,255,0.06)",
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.04)",
            zeroline=False,
            tickfont=dict(color="#475569", size=11),
            tickprefix="$",
            tickformat=",.0f",
            showline=False,
        ),
        legend=dict(
            orientation="h",
            x=0, y=1.06,
            font=dict(color="#94a3b8", size=12),
            bgcolor="rgba(0,0,0,0)",
            itemclick="toggleothers",
        ),
        margin=dict(l=10, r=10, t=36, b=10),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#1e293b",
            bordercolor="rgba(255,255,255,0.08)",
            font_color="#e2e8f0",
            font_size=13
        ),
        height=400,
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)