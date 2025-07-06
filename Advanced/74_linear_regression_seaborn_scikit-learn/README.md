# Linear Regression and Data Visualization with Seaborn (Movie Budget vs Revenue Analysis)

## Project Overview

This project analyzes the relationship between movie production budgets and worldwide box office revenues. Using a dataset of movie budgets and revenues, the goal is to investigate whether higher budgets generally lead to higher revenues, helping answer whether studios should invest more in production to maximize box office success.

---

## Key Features and Learning Outcomes

- Data cleaning techniques including removing unwanted characters from multiple columns.
- Filtering datasets using Pandas `.loc[]` and `.query()` based on multiple conditions.
- Creating advanced visualizations such as bubble charts with Seaborn, integrating three dimensions (budget, release date, revenue).
- Styling Seaborn visualizations using built-in themes and Matplotlib customizations.
- Using floor division to group movie release years into decades for temporal analysis.
- Visualizing relationships with scatter plots and superimposed linear regression lines using Seaborn.
- Interpreting regression fit quality using R-squared metrics.
- Running custom linear regression models using scikit-learn and deriving model coefficients.
- Using regression models to make revenue predictions based on production budgets.

---

## Getting Started

### Installation

This project requires Python and the following packages:

- pandas
- matplotlib
- seaborn
- scikit-learn

Install dependencies via pip:

```
pip install pandas matplotlib seaborn scikit-learn
```

### Dataset

`cost_revenue_dirty.csv` is used as the primary dataset containing movie production budgets, release dates, and revenue figures. Data cleaning steps are included to parse and format monetary values and dates correctly.

---

## Project Structure

- **Data Cleaning:** Preparing the raw dataset by removing extraneous characters, converting data types, and filtering unreleased films.
- **Exploratory Data Analysis:** Generating descriptive statistics and answering questions related to budget and revenue distributions.
- **Visualizations:** Creating scatter plots, bubble charts, and styled regression plots to understand trends visually.
- **Modeling:** Using scikit-learn to perform linear regression and evaluate model fit.
- **Interpretation:** Drawing insights about the relationship between budget and revenue and making predictions.

---

## Usage

Open the Jupyter Notebook and run each section in order to:

- Load and clean the data.
- Explore and plot relationships.
- Fit regression models.
- Evaluate and interpret results.

Visualizations and results update interactively in the notebook.

---

## Future Work

- Extend models to include more explanatory variables (e.g., genre, marketing spend).
- Explore non-linear regression models or machine learning methods.
- Incorporate international box office details and critical reception metrics.
- Develop interactive dashboards for dynamic analysis.

---

## Acknowledgments

This project was developed based on publicly available movie budget and revenue data as well as widely used Python libraries for data science and visualization.

---

## License

This project is open source and available under the MIT License.

---

## Contact

For questions or contributions, please reach out via GitHub issues or email.

---

Thank you for exploring the movie budget versus revenue dynamics with this project!
