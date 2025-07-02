# LEGO Data Analysis with Pandas & Matplotlib

## Overview

This project explores the LEGO dataset, focusing on aggregation, merging, and visualization skills using Pandas and Matplotlib in a Jupyter Notebook. Through guided challenges, we analyze LEGO's product history, set complexity, and theme evolution.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Motivation & Key Questions](#project-motivation--key-questions)
3. [Data](#data)
4. [Getting Started](#getting-started)
5. [Analysis Workflow](#analysis-workflow)
6. [Visualization Examples](#visualization-examples)
7. [Learning Points & Summary](#learning-points--summary)
8. [Requirements](#requirements)
9. [License](#license)

---

## Introduction

This notebook-based project demonstrates how to:
- Read and explore multiple CSV datasets on LEGO sets, themes, and parts.
- Aggregate and analyze historical data.
- Merge relational data sources.
- Visualize trends using a variety of chart types.

---

## Project Motivation & Key Questions

Some business and historical questions analyzed in the notebook:
- What is the most enormous LEGO set ever created and how many parts did it have?
- When were the first LEGO sets released and how many sets did the company sell initially?
- Which LEGO theme has the most sets?
- How did LEGO's product line grow over time?
- Do older LEGO sets have more or fewer parts than newer sets?
- How do the number of themes and sets released each year compare?

---

## Data

The project uses open LEGO datasets containing tables on:
- `sets.csv` (LEGO set details)
- `themes.csv` (theme metadata)
- `colors.csv` (used for warm-up challenge)

---

## Getting Started

1. Clone the repository:

2. Install dependencies (preferably in a virtual environment):
    ```
    pip install pandas matplotlib
    ```

3. Launch Jupyter Notebook:
    ```
    jupyter notebook
    ```
Open and run the notebook step by step, following the Markdown prompts and supplying code solutions as needed.

---

## Analysis Workflow

The project covers:

- Embedding images using HTML `<img>` tags.
- Applying Markdown and section headings for clear structure.
- Aggregating data with `.groupby()`, `.count()`, `.agg()`, and `.value_counts()`.
- DataFrame slicing (e.g. `df[:10]`).
- Renaming columns with `.rename()`.
- Line plots with dual axes (`.twinx()`) for trends of different scales.
- Scatter plot creation using Matplotlib.
- Understanding primary/foreign key concepts and merging DataFrames with `.merge()`.
- Customizing and plotting bar charts for categorical comparisons.

---

## Visualization Examples

- **Line and Bar Charts:** Compare the number of LEGO sets vs. number of themes by year.
- **Dual Axis Plot:** Visualize both metrics on separate y-axes for clarity.
- **Bar Chart (Top Themes):** Largest LEGO themes by set count, revealing business trends and product diversification.

---

## Learning Points & Summary

**Key skills learned:**
- HTML Markdown for headings and images in Notebooks
- Aggregation with `.groupby()` + `.count()`, `.agg()`, `.value_counts()`
- DataFrame slicing and column renaming
- Merging DataFrames with `.merge()`
- Creating and customizing line, bar, and scatter plots with Matplotlib
- Working with relational-style tables (primary & foreign keys)

---

## Requirements

- Python 3.x
- pandas
- matplotlib
- Jupyter Notebook

---

## License

This project is for educational purposes.

---

**Feel free to fork and extend!**
