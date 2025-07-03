# Google Trends & Real-World Time Series: Data Analysis and Visualization

This project explores how Google search interest, as captured by Google Trends, relates to real-world financial and economic time series data. Datasets include web search interest for "Bitcoin", "Tesla", and "Unemployment Benefits", along with corresponding price or rate data for each topic.

---

## Project Overview

**What can the popularity of search terms tell us about the world?**  
By combining Google Trends data with financial and economic indicators, this project investigates:

- How search volume for "Bitcoin" relates to Bitcoin's price
- How search interest in "Tesla" relates to Tesla's stock price
- How searches for "Unemployment Benefits" vary with the actual unemployment rate in the United States

---

## Features and Concepts

- **Descriptive Statistics:**  
  Quickly summarizing datasets with `.describe()` to get a sense of distribution and outliers.

- **Data Cleaning:**  
  Identifying and removing missing values using `.isna().values.any()`, `.isna().values.sum()`, and `.dropna()`.

- **Datetime Parsing & Resampling:**  
  Converting date columns to `datetime` objects for robust time series handling.  
  Resampling data (e.g., from daily to monthly) with `.resample()` for comparison between different periodicities.

- **Advanced Visualization (Matplotlib):**
  - Fine-tuned chart resolution with `figsize` and `dpi`
  - Custom line styles (`'--'`, `'-.'`) and markers (`'o'`, `'^'`, etc.)
  - Locators and formatters from `matplotlib.dates` for precise time-based tick marks
  - Custom colors using named values and HEX codes
  - Axis labeling, limits, and chart titles for clear presentation
  - Enabling `.grid()` to reveal seasonality

- **Insights:**  
  - Uncovered strong correlations between search spikes and price/rate movements (notably during crises).
  - Detected seasonality in unemployment search trends.
  - Observed historical events like the 2008 financial crisis and 2020 pandemic in both search and price/rate data.

---

## Project Structure

- Jupyter Notebook: Contains all exploratory data analysis, code, visualizations, and interpretation.
- Data files (.csv):  
  - Tesla weekly/monthly web search and price  
  - Bitcoin daily/monthly price, web search  
  - Unemployment monthly data and web search

---

## How to Use

1. Clone or download this repository.
2. Place the required `.csv` files in the same directory as the notebook.
3. Open the notebook and run cells sequentially to reproduce data exploration and visualization.
4. Modify and extend the notebook for new queries or additional datasets.

---

## Requirements

- Python 3.8+
- pandas
- matplotlib

Install requirements via pip if needed:

```
pip install pandas matplotlib
```

---

## License

This project is for educational and demonstrative purposes.

---

## Acknowledgments

- Google Trends for search interest data
- Yahoo Finance & FRED for price and economic datasets

---

*Happy analyzing!*
