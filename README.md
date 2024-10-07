# Asg-5-Scipy
# NBA Player Statistics Analysis

## Purpose
This project aims to analyze NBA player statistics over multiple seasons to identify trends and insights. The analysis includes calculating various statistical measures, performing linear regression, and visualizing data to understand player performance, particularly focusing on three-point accuracy and other key metrics.

## Project Structure
The project is structured as a Python script that performs the following tasks:

1. **Data Loading and Preparation**
   - Load the dataset containing player statistics.
   - Filter the data to include only regular season statistics.

2. **Player Analysis**
   - Identify the player with the most regular seasons played.
   - Calculate and visualize the three-point accuracy for this player over the seasons.

3. **Statistical Analysis**
   - Calculate average three-point accuracy and the actual average number of three-pointers made.
   - Perform linear interpolation to fill missing values in the dataset.
   - Calculate statistical measures (mean, variance, skewness, kurtosis) for field goals made (FGM) and field goals attempted (FGA).
   - Conduct paired t-tests and individual t-tests to compare FGM and FGA.

## Class Design and Implementation
The project does not currently use classes, but if we were to refactor it into an object-oriented design, we might consider the following classes:

### `PlayerStatsAnalyzer`
- **Attributes:**
  - `data`: The dataset containing player statistics.
  - `player_name`: The name of the player being analyzed.
  - `player_data`: Filtered data for the specific player.
  
- **Methods:**
  - `__init__(self, file_path)`: Initializes the analyzer with the dataset file path.
  - `load_data(self)`: Loads the dataset from the specified file path.
  - `filter_regular_season(self)`: Filters the dataset to include only regular season data.
  - `find_most_seasons_player(self)`: Identifies the player with the most regular seasons played.
  - `calculate_three_point_accuracy(self)`: Calculates three-point accuracy for the player.
  - `perform_linear_regression(self)`: Performs linear regression on the player's three-point accuracy.
  - `plot_three_point_accuracy(self)`: Plots the three-point accuracy over the seasons.
  - `calculate_statistics(self)`: Calculates various statistical measures for FGM and FGA.
  - `perform_t_tests(self)`: Conducts paired and individual t-tests for FGM and FGA.

### `DatasetInterpolator`
- **Attributes:**
  - `data`: The dataset containing player statistics.
  
- **Methods:**
  - `__init__(self, data)`: Initializes the interpolator with the dataset.
  - `interpolate_missing_values(self)`: Performs linear interpolation to fill missing values.
  - `reset_index(self)`: Resets the index of the dataset after interpolation.

## Limitations
- The analysis assumes that the dataset is clean and does not handle potential data quality issues such as missing or incorrect values.
- The linear regression model is simplistic and does not account for potential confounding variables.
- The project currently focuses on a single player with the most seasons played, which may not provide a comprehensive view of overall trends in the NBA.

## Usage
To run the analysis, execute the Python script. Ensure that the dataset file path is correctly specified in the script.

```bash
python nba_player_stats_analysis.py
```

## Dependencies
- pandas
- numpy
- scikit-learn
- scipy
- matplotlib

Install the dependencies using pip:

```bash
pip install pandas numpy scikit-learn scipy matplotlib
```

## Conclusion
This project provides a framework for analyzing NBA player statistics over multiple seasons. By refactoring the script into an object-oriented design, we can improve code organization and maintainability, making it easier to extend the analysis to include additional players and metrics.
