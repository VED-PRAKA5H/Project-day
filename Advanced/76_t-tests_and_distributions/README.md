# The Tragic Discovery of Handwashing: t-Tests & Distributions

This is a data science project that revisits the pioneering work of Dr. Ignaz Semmelweis, a 19th-century Hungarian physician who discovered the profound impact of handwashing on reducing maternal mortality from childbed fever at the Vienna General Hospital in the 1840s.

---

## Project Overview

The project uses historical birth and death records from the Vienna General Hospital maternity clinics to:

- Explore and clean the data, understanding births and deaths over time.
- Compare maternal death rates between two hospital clinics staffed differently.
- Analyze the effect of Dr. Semmelweis’ introduction of mandatory handwashing.
- Visualize distributions of death rates using histograms, box plots, and Kernel Density Estimates (KDE).
- Conduct statistical significance testing (t-tests) to robustly validate the impact of handwashing.
- Tell the compelling historical narrative supported by data-driven insights and visualizations.

---

## Key Features

- **Data Exploration:** Examination of birth and death data by year, month, and clinic.
- **Visualization:** Interactive and static charts using Plotly and Matplotlib (line charts, histograms, box plots, KDE plots).
- **Statistical Analysis:** Calculation of death rate percentages, rolling averages, and hypothesis testing using SciPy.
- **Insights on Public Health:** Quantitative evidence showing the drastic reduction in maternal deaths after implementing handwashing protocols.
- **Historical Context:** The tragic story of Dr. Semmelweis’ struggle to convince the medical community despite overwhelming evidence.

---

## Technologies Used

- Python 3.x
- Pandas for data manipulation
- NumPy for conditional data processing
- Matplotlib and Seaborn for static visualizations
- Plotly Express for interactive visualizations
- SciPy for statistical hypothesis testing

---

## Project Structure

- **Data Cleaning & Exploration:** Initial data inspection and summary statistics.
- **Clinic Comparison:** Analysis of yearly births and deaths between Clinic 1 (doctors) and Clinic 2 (midwives).
- **Handwashing Impact:** Calculations and visualizations highlighting death rate reductions before and after the introduction of handwashing.
- **Statistical Testing:** T-tests confirming statistical significance of handwashing effect.
- **Final Summary:** Learning points, reflections, and the story of Semmelweis.

---

## How to Use

1. Clone this repository.
2. Load the datasets (`df_yearly` and `df_monthly`) as Pandas DataFrames.
3. Run the Jupyter Notebook step-by-step to explore data, generate plots, and perform statistical tests.
4. Visualizations and statistical results will clearly demonstrate the historical impact of handwashing in reducing maternal mortality.

---

## Acknowledgments

This project pays homage to Dr. Ignaz Semmelweis and his groundbreaking contributions to medical hygiene and public health.

Data and historical context were sourced from publicly available archives and research on 19th-century Vienna General Hospital records.

---

## License

This project is open source and free to use under the MIT License.

---

## Contact

For questions or collaboration, please open an issue or contact the author.

---

Thank you for exploring this important historical medical data science project!