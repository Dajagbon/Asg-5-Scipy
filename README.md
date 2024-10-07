# Asg-5-Scipy
### README.md

# NBA Player Statistics Analysis

## Project Overview

This project aims to analyze NBA player statistics over multiple seasons. The analysis includes calculating various statistical measures, performing linear regression, and conducting t-tests on the data. The project is implemented in Python using libraries such as pandas, numpy, scikit-learn, scipy, and matplotlib.

## Purpose

The primary purpose of this project is to:
1. Identify the player with the most regular seasons played.
2. Calculate and visualize the three-point accuracy of the identified player over the seasons.
3. Interpolate missing values for specific seasons.
4. Calculate statistical measures such as mean, variance, skewness, and kurtosis for field goals made (FGM) and field goals attempted (FGA).
5. Perform paired and individual t-tests on FGM and FGA data.

## Class Design and Implementation

### Data Loading and Filtering

- **Load the dataset**: The dataset is loaded from a CSV file containing player statistics.
- **Filter for NBA regular season data**: Only data from the regular season is considered for analysis.

### Player Identification

- **Identify the player with the most seasons played**: The player with the highest number of regular seasons played is identified.

### Three-Point Accuracy Calculation

- **Calculate three-point accuracy**: The three-point accuracy for each season is calculated for the identified player.
- **Linear regression**: Linear regression is performed on the three-point accuracy data to identify trends over the seasons.
- **Visualization**: The three-point accuracy data and the line of best fit are plotted.

### Interpolation of Missing Values

- **Extract the starting year from the Season column**: The starting year is extracted from the Season column.
- **Interpolate missing values**: Missing values for specific seasons are interpolated using linear interpolation.

### Statistical Measures Calculation

- **Calculate statistical measures**: Mean, variance, skewness, and kurtosis are calculated for FGM and FGA.

### T-Tests

- **Paired t-test**: A paired t-test is performed on FGM and FGA data.
- **Individual t-tests**: Individual t-tests are performed against the sample mean for FGM and FGA.

## Class Attributes and Methods

### Attributes

- [`players_stats_by_season_full_details`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A102%2C%22character%22%3A6%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): DataFrame containing the player statistics.
- `nba_regular_season_data`: DataFrame containing filtered data for the regular season.
- `seasons_played`: Series containing the number of seasons played by each player.
- `most_seasons_player`: String containing the name of the player with the most seasons played.
- `player_data`: DataFrame containing data for the identified player.
- `X`: Numpy array containing three-point accuracy data for linear regression.
- `y`: Numpy array containing season data for linear regression.
- `model`: LinearRegression object for performing linear regression.
- `y_pred`: Numpy array containing predicted values for the line of best fit.
- `sum_accuracy`: Float containing the sum of three-point accuracy over the played seasons.
- `number_of_seasons`: Integer containing the number of seasons played.
- `average_accuracy`: Float containing the average three-point accuracy.
- `average_3PM`: Float containing the actual average number of three-pointers made.
- `fgm_mean`: Float containing the mean of FGM.
- `fgm_variance`: Float containing the variance of FGM.
- `fgm_skew`: Float containing the skewness of FGM.
- `fgm_kurtosis`: Float containing the kurtosis of FGM.
- [`fga_mean`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A99%2C%22character%22%3A21%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the mean of FGA.
- [`fga_variance`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A99%2C%22character%22%3A43%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the variance of FGA.
- [`fga_skew`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A99%2C%22character%22%3A65%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the skewness of FGA.
- [`fga_kurtosis`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A99%2C%22character%22%3A87%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the kurtosis of FGA.
- [`t_stat_rel`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A106%2C%22character%22%3A0%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the t-statistic for the paired t-test.
- [`p_value_rel`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A106%2C%22character%22%3A12%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the p-value for the paired t-test.
- [`t_stat_fgm`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A109%2C%22character%22%3A0%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the t-statistic for the individual t-test on FGM.
- [`p_value_fgm`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A109%2C%22character%22%3A12%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the p-value for the individual t-test on FGM.
- [`t_stat_fga`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A110%2C%22character%22%3A0%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the t-statistic for the individual t-test on FGA.
- [`p_value_fga`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fdanie%2FDownloads%2Ftest%201.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A110%2C%22character%22%3A12%7D%7D%5D%2C%22f4202b51-5692-43e2-956a-382ca892c874%22%5D "Go to definition"): Float containing the p-value for the individual t-test on FGA.

### Methods

- `load_data()`: Loads the dataset from a CSV file.
- `filter_regular_season_data()`: Filters the data for the regular season.
- `identify_most_seasons_player()`: Identifies the player with the most regular seasons played.
- `calculate_three_point_accuracy()`: Calculates the three-point accuracy for each season.
- `perform_linear_regression()`: Performs linear regression on the three-point accuracy data.
- `plot_three_point_accuracy()`: Plots the three-point accuracy data and the line of best fit.
- `interpolate_missing_values()`: Interpolates missing values for specific seasons.
- `calculate_statistics()`: Calculates statistical measures for FGM and FGA.
- `perform_t_tests()`: Performs paired and individual t-tests on FGM and FGA data.

## Limitations

- The dataset must be in a specific format with columns such as 'Player', 'Stage', 'Season', '3PM', '3PA', 'FGM', and 'FGA'.
- The interpolation method used is linear, which may not be suitable for all types of data.
- The analysis is limited to regular season data and does not consider playoff or other stages.
- The t-tests assume that the data is normally distributed, which may not always be the case.

## Conclusion

This project provides a comprehensive analysis of NBA player statistics, focusing on three-point accuracy, statistical measures, and t-tests. The implementation is modular and can be extended to include additional analyses or visualizations as needed.
