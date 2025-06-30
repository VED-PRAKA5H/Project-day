# College Major Salary Analysis

## Project Overview  
This project explores a dataset of college majors and their associated salary statistics. The goal is to analyze the data to find insights such as highest and lowest salaries, salary risks, and group-level salary trends.

***

## Learning Points & Summary

### Data Exploration  
- Use `.head()`, `.tail()`, `.shape`, and `.columns` to explore your DataFrame, understand its structure, find the number of rows and columns, and check column names.  
- Identify missing or invalid data using `.isna()` and clean the DataFrame with `.dropna()`.

### Data Access  
- Access entire columns using square bracket notation: `df['column name']` or multiple columns: `df[['column 1', 'column 2']]`.  
- Access individual cells by chaining: `df['column name'][index]` or with `.loc`: `df['column name'].loc[index]`.

### Summary Statistics  
- Find maximum and minimum values and their positions using `.max()`, `.min()`, `.idxmax()`, and `.idxmin()`.  
- Sort values with `.sort_values()`.  
- Add new calculated columns using `.insert()`.

### Grouping and Aggregation  
- Use `.groupby()` to create Excel-style pivot tables by grouping entries by categories (e.g., STEM, Business, HASS).  
- Grouping allows counting entries and calculating aggregates like mean salaries.

***

## Key Methods Used  
- Data inspection: `head()`, `tail()`, `shape`, `columns`  
- Missing data handling: `isna()`, `dropna()`  
- Data selection: square brackets, `loc`  
- Descriptive stats: `max()`, `min()`, `idxmax()`, `idxmin()`  
- Sorting and column insertion: `sort_values()`, `insert()`  
- Grouping data: `groupby().count()`, `groupby().mean()`  

***

## Usage  
1. Upload `salaries_by_college_major.csv` to the notebook.  
2. Load data with `pandas.read_csv()`.  
3. Explore and clean data as per walkthrough.  
4. Perform salary analyses and grouping queries to gain insights.

***

## Conclusion  
This project offers practical data science skills for exploring and analyzing real-world tabular data using pandas, focusing on data cleaning, indexing, aggregation, and group-wise summaries.
