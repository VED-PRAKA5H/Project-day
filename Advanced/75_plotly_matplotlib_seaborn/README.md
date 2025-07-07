# Nobel Prize Data Analysis using plotly, matplotlib and seaborn

This project explores patterns and trends in Nobel Prize awards, leveraging data science techniques to uncover insights into laureates, research organizations, and global scientific achievements. All analysis and visualizations are documented in interactive Jupyter Notebook format.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Data Science Techniques](#data-science-techniques)
- [Installation](#installation)
- [Usage](#usage)
- [Notebooks](#notebooks)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This repository demonstrates a complete exploratory analysis of the Nobel Prize dataset, tackling questions like:

- Which countries and organizations have produced the most laureates?
- How do prize categories differ in terms of winners?
- What are trends in laureate age, prize sharing, and discovery locations?
- How have patterns shifted over time?

Interactive visualizations (bar charts, choropleth maps, sunburst charts, box plots, regression plots) bring these insights to life.

---

## Features

- Missing value detection and handling
- Data type conversions for robust analysis
- Rolling averages to smooth time series data
- Donut, bar, and stacked bar charts (Plotly)
- Choropleth maps for geographic visualizations
- Sunburst charts showing hierarchical organization-country-city relationships
- Age analysis of laureates, including descriptive statistics
- Seaborn histograms and box plots for distribution analysis
- Regression and trend analysis with Seaborn’s `regplot` and `lmplot`

---

## Data Science Techniques

- Pandas aggregation: `.groupby()`, `.value_counts()`, `.merge()`, `.agg()`, `.sort_values()`
- Visualization: Plotly (`bar`, `donut`, `choropleth`, `sunburst`), Seaborn (`histplot`, `boxplot`, `regplot`, `lmplot`)
- Handling and interpreting NaN values
- Feature engineering (winning age, prize share, etc.)
- Comparative and segmented analysis across countries, categories, and organizations

---

## Installation

1. Clone this repository:

2. Install required dependencies (recommended: use a virtual environment):

    ```
    pip install pandas numpy matplotlib seaborn plotly
    ```

---

## Usage

1. Download or obtain the Nobel Prize dataset (e.g., as a CSV file).
2. Launch Jupyter Notebook.
3. Open `EDA.ipynb` (or the main notebook for this project).
4. Follow and run the cells to reproduce the entire analysis, view visualizations, and experiment with additional questions.

---

## Notebooks

- `EDA.ipynb`: Main notebook containing all sections:
    - Data cleaning and exploration
    - Country, city, and organization analysis
    - Prize category and gender breakdowns
    - Time series and rolling average analysis
    - Age analysis, regression, and box plots
    - Interactive visualizations and insights

---

## Data

- **Dataset:** (Provide details, e.g. source URL, CSV filename, preprocessing steps if any)
    - For best results, ensure fields include birth and organization location information, ISO country codes, category, prize share, birth date, year, sex, etc.

---

## Contributing

Contributions welcome! Please open issues for bugs, suggestions, or new analysis ideas.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Explore, analyze, and visualize Nobel Prize data to reveal deeper insights into scientific achievement and global patterns!**