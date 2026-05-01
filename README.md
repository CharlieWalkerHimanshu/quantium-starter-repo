# 🍬 Soul Foods Pink Morsel Sales Dashboard

A fully interactive sales analytics dashboard built with **Python**, **Dash**, and **Plotly** as part of the Quantium Data Analytics Virtual Experience Program.

---

## 📸 Overview

This project ingests raw daily sales data, processes it into a clean dataset, and renders a polished dark-themed dashboard where users can explore Pink Morsel revenue trends across all four regions — individually or in any combination.

---

## 🚀 Features

- **Multi-region comparison** — toggle any combination of North, East, South, and West regions simultaneously; each region gets its own distinct colored line
- **KPI stat cards** — Total Revenue, Peak Sales Day, and Regions Tracked computed directly from the data
- **Interactive chart** — hover tooltips with region + date + revenue, legend click to isolate a single region
- **Dark UI** — modern near-black theme with gradient typography, animated stat cards, and a responsive grid layout
- **Automated tests** — 3 Selenium-based integration tests verifying the header, chart, and region picker are rendered

---

## 🗂️ Project Structure

```
quantium-starter-repo/
├── app.py                    # Dash app — layout, callbacks, chart config
├── process_data.py           # ETL script: reads raw CSVs → formatted_sales_data.csv
├── formatted_sales_data.csv  # Processed output (sales, date, region)
├── requirements.txt          # Pinned dependencies
├── run_tests.sh              # CI helper: activates venv and runs pytest
├── assets/
│   └── style.css             # Full dark-theme stylesheet (Inter font, gradient, cards)
├── data/
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   └── daily_sales_data_2.csv
└── tests/
    ├── conftest.py           # sys.path setup for imports
    └── test_app.py           # Dash integration tests (dash_duo + Selenium)
```

---

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/CharlieWalkerHimanshu/quantium-starter-repo.git
cd quantium-starter-repo
```

### 2. Create a virtual environment
```bash
# Windows
py -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Process the raw data (only needed once)
```bash
python process_data.py
```

### 5. Run the dashboard
```bash
python app.py
```

Open **http://127.0.0.1:8050/** in your browser.

---

## 🧪 Running Tests

```bash
# Windows (PowerShell)
.\venv\Scripts\activate
pytest

# macOS / Linux
bash run_tests.sh
```

Tests use `dash_duo` (Selenium) and verify:
- `#header` is present in the DOM
- `#sales-chart` renders
- `#region-picker` checklist is present

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Dashboard framework | Dash 4.0 |
| Charting | Plotly 6 |
| Data processing | pandas 3 |
| Styling | CSS3 (Inter font, CSS Grid, CSS variables) |
| Testing | pytest + Selenium (`dash_duo`) |

---

## 📊 Data Pipeline

`process_data.py` performs the following steps:

1. Reads `data/daily_sales_data_0/1/2.csv` and concatenates them
2. Filters to `product == "pink morsel"` only
3. Strips `$` from the `price` column and converts to float
4. Calculates `sales = quantity × price`
5. Outputs a clean 3-column CSV: `sales`, `date`, `region`

---

## 📄 License

This project was built as part of the [Quantium Data Analytics Virtual Experience](https://www.theforage.com/simulations/quantium/data-analytics-rqkb) on Forage.
