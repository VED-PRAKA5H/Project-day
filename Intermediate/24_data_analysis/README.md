# Data Analysis Notebooks

**Perform exploratory data analysis on real-world datasets with Python’s pandas library. Includes examples with weather data and the 2018 Central Park Squirrel Census.**

***

### Features

- **Downloadable Dataset:** Easily access the [2018 Central Park Squirrel Census - Squirrel Data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data).
- **Weather Data Analysis:** Learn the basics of pandas with a small, sample weather dataset-explore data types, calculate statistics, filter data, and more.
- **Advanced Census Analysis:** Deep dive into the squirrel census, including aggregating fur color counts and saving results to CSV.
- **Practical DataOps:** Create your own DataFrame, save it to CSV, and apply column-wise transformations using pandas' intuitive API.

***

### Project Structure

```
Data-Analysis/
│── pandas_analysis.ipynb                                      # Main Jupyter notebook for all analysis
│── weather_data.csv                                           # Sample weather dataset
│── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv     # Squirrel census dataset (download link above)
│── data.csv                                               # Squirrel fur color count results (generated)
│── new_data.csv                                            # Sample exported dataframe
│── README.md                                             # Project documentation
```

***

### How It Works

- Explore the basics of pandas: loading data, inspecting types, filtering columns/rows, and simple statistics.
- Apply Python functions to create new features (e.g., converting temperature to Fahrenheit).
- Analyze the squirrel dataset to count populations by fur color and export results for visualization or further use.
- All analysis documented in an interactive notebook—no complex setup required.

***

### Requirements

- **Python 3.x**
- **pandas** 
- Jupyter Notebook (`pip install notebook`)
- Download the squirrel census dataset as directed above.

***

### Usage Instructions

1. Clone this repository and download the datasets.
2. Open the notebook:  
    - In terminal, run: `jupyter notebook pandas_analysis.ipynb`
3. Walk through the code and outputs, modifying or adding steps to suit new data or analysis goals.
4. Results (such as custom CSV exports) will appear in the project directory.

***

### References

- **2018 Central Park Squirrel Census - Squirrel Data:**  
  [NYC Open Data (official download)](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)
- **pandas documentation:**  
  [pandas user guide & API reference](https://pandas.pydata.org/docs/)
