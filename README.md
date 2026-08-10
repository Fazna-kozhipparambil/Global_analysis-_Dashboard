#  Global Temperature Anomalies Dashboard

An interactive Streamlit dashboard for exploring global temperature anomaly data — filter by year range, switch between visualization types, and inspect trends, correlations, and distributions.

## Features

- **Year range filter** — slice the dataset to any range via a sidebar slider
- **Multiple visualizations**, selectable from the sidebar:
  - **Line Plot** — annual anomalies over time, plus a five-year vs. ten-year anomaly comparison
  - **Scatter Plot** — monthly anomaly vs. monthly uncertainty
  - **Heatmap** — correlation matrix across all numeric variables
- **Distribution view** — histogram of annual temperature anomalies
- **Live data table** — view the filtered rows directly in the app

## Tech Stack

- [Streamlit](https://streamlit.io/) — app framework
- [Pandas](https://pandas.pydata.org/) — data handling
- [Plotly Express](https://plotly.com/python/plotly-express/) — interactive charts

## Dataset

`Global Temperature.csv` — historical global temperature anomaly records, including annual, five-year, ten-year, and monthly anomaly figures along with monthly uncertainty values.

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
# Clone the repo
git clone https://github.com/Fazna-kozhipparambil/Global_analysis-_Dashboard.git
cd Global_analysis-_Dashboard

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run global_temperature_visualization_dashboard.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`.

## Usage

1. Use the sidebar slider to select a year range.
2. Choose a visualization type — **Line Plot**, **Scatter Plot**, or **Heatmap**.
3. Scroll down to view the distribution of annual anomalies for the selected range.
4. Explore the filtered data table for the underlying numbers.

## Project Structure

```
Global_analysis-_Dashboard/
├── Global Temperature.csv                        # Dataset
├── global_temperature_visualization_dashboard.py  # Streamlit app
├── requirements.txt                               # Python dependencies
└── README.md
```

## Possible Improvements

- [ ] Cache data loading with `@st.cache_data` for faster reruns
- [ ] Strip whitespace from CSV column headers on load
- [ ] Add axis units (°C) and richer chart labels
- [ ] Handle empty date ranges gracefully
- [ ] Add a regional/country-level breakdown if the dataset supports it

## Author

**Fazna Kozhipparambil**
[GitHub](https://github.com/Fazna-kozhipparambil)

## License

This project is open source and available under the [MIT License](LICENSE).
