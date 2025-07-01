# Programming Language Popularity Visualization

## Project Overview
This project visualizes the popularity of different programming languages over time using data from Stack Overflow posts. By analyzing tagged posts over the years, the project provides insights into trends and shifts in language popularity through interactive and styled line charts.

## Features
- Data cleaning and preprocessing using Pandas, including converting string dates to datetime objects.
- Data reshaping with the Pandas `.pivot()` method to organize languages as columns and dates as rows.
- Handling missing data by filling NaN values with zeros.
- Creating multi-line charts with Matplotlib to compare language popularity across time.
- Adding legends, labels, and custom styling for readability.
- Smoothing noisy time-series data using rolling averages for better trend visualization.

## Technologies Used
- Python 3.x
- Pandas for data manipulation
- Matplotlib for data visualization

## Getting Started

### Prerequisites
Make sure you have Python installed along with the following packages:
- pandas
- matplotlib

Install them via pip if needed:

```shell
pip install pandas matplotlib
```

### Running the Project
1. Load your dataset containing Stack Overflow posts tagged by programming language.
2. Execute preprocessing steps to clean and reshape the data.
3. Use the included scripts or notebook cells to generate line charts of language popularity.
4. Experiment with smoothing parameters to visualize trends more clearly.

## Code Highlights

- Convert string dates to datetime objects for plotting:
  `df['DATE'] = pd.to_datetime(df['DATE'])`

- Reshape data with `.pivot()` to get languages as columns:
  `reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')`

- Fill missing data with zeros:
  `reshaped_df.fillna(0, inplace=True)`

- Plot multiple languages with legends:
  ```python
  plt.figure(figsize=(16,10))
  for column in reshaped_df.columns:
      plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)
  plt.legend(fontsize=16)
  plt.show()
  ```

- Smooth data with rolling averages:
  `roll_df = reshaped_df.rolling(window=6).mean()`

## Contribution
Contributions are welcome! Feel free to submit issues or pull requests for improvements or additional features.

## License
This project is licensed under the MIT License.
