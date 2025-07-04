# Android App Store Data Analysis and Visualization with Plotly

## Overview

This project analyzes and visualizes data from the Google Play Store to uncover insights about app categories, popularity, pricing strategies, and revenue potential. We explore thousands of apps to understand market competitiveness, app installs, and how free vs. paid apps perform across different categories.

The dataset includes app metadata such as categories, genres, ratings, installs, prices, and more, which we clean and transform for meaningful analysis.

The project uses Python with Pandas for data wrangling and Plotly for creating interactive and beautiful charts including pie charts, bar charts, scatter plots, and box plots.

---

## Features

- Data cleaning techniques:
  - Removing duplicates using `.duplicated()` and `.drop_duplicates()`
  - Handling missing values and converting columns to numeric types with `.to_numeric()`
- Exploratory Data Analysis (EDA):
  - Sampling and preliminary data overview
  - Investigation of ratings, installs, app sizes, and content ratings
- Data visualization using Plotly:
  - Pie and donut charts for content rating distribution
  - Bar charts showing app competitiveness and category popularity
  - Scatter plots to compare app category competitiveness vs popularity
  - Grouped bar charts for free vs paid apps by category
  - Box plots to compare installs and revenue between free and paid apps
  - Analysis of price distribution across paid app categories
- Insightful business questions answered regarding app store dynamics and monetization strategies

---

## Installation

1. Clone this repository:

2. Navigate into the project directory:
3. Install required Python packages (recommended within a virtual environment):
   ```
   pip install pandas plotly
   ```

---

## Usage

Open the Jupyter Notebook provided  and run the cells step-by-step to reproduce the data cleaning, analysis, and visualizations.

You can modify the notebook to explore additional analyses or different datasets.

---

## Dataset

The dataset consists of Google Play Store app metadata collected during 2017/2018. It includes information on:

- App name, category, and genres
- Ratings and number of reviews
- Number of installs (approximate)
- Price and type (Free or Paid)
- Size and content rating

---

## Insights

- The **Family** and **Games** categories are highly competitive with many apps.
- **Games** and **Tools** receive the most downloads (popularity).
- Paid apps tend to have significantly fewer installs compared to free apps.
- Median paid app revenue generally does not recoup typical development costs, with some category exceptions.
- Pricing varies widely across categories, with Medical and Business apps commanding higher prices.

---


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Data inspired from Google Play Store analytics
- Plotly documentation and examples for visualization guidance
- Articles on app pricing and development cost for business context
