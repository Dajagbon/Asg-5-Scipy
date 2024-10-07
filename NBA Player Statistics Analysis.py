import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import skew, kurtosis, ttest_rel, ttest_1samp
import matplotlib.pyplot as plt

# Load the dataset
players_stats_by_season_full_details = pd.read_csv('C:/Users/danie/Downloads/Pythonclasstwo/players_stats_by_season_full_details.csv')

# Filter for NBA regular season data
nba_regular_season_data = players_stats_by_season_full_details[players_stats_by_season_full_details['Stage'] == 'Regular_Season']

# Count the number of seasons each player has played
seasons_played = nba_regular_season_data.groupby('Player')['Stage'].nunique()

# Find the player with the most seasons played
most_seasons_player = seasons_played.idxmax()
print(f"The player with the most regular seasons is: {most_seasons_player}")

# Filter data for the player with the most seasons and create a copy
player_data = nba_regular_season_data[nba_regular_season_data['Player'] == most_seasons_player].copy()

# Calculate three-point accuracy for each season
player_data['three_point_accuracy'] = player_data['3PM'] / player_data['3PA']

# Display the three-point accuracy for each season
print(player_data[['Stage', 'three_point_accuracy']])

# Prepare data for linear regression
X = player_data['three_point_accuracy'].values.reshape(-1, 1)
y = player_data['Season'].apply(lambda season: int(season.split('-')[0])).values

# Perform linear regression
model = LinearRegression()
model.fit(X, y)

# Predict values for the line of best fit
y_pred = model.predict(X)

# Plot the data and the line of best fit
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Line of Best Fit')
plt.xlabel('Three-Point Accuracy')
plt.ylabel('Season')
plt.title(f'Three-Point Accuracy Over Seasons for {most_seasons_player}')
plt.legend()
plt.show()

# Extract the starting year from the Season column
players_stats_by_season_full_details['Season'] = players_stats_by_season_full_details['Season'].str.split(' - ').str[0].astype(int)

# Calculate the average 3-point accuracy over the seasons
players_stats_by_season_full_details['3PA'] = players_stats_by_season_full_details['3PA'].astype(float)  # Ensure the accuracy column is in float

earliest_season = players_stats_by_season_full_details['Season'].min()
latest_season = players_stats_by_season_full_details['Season'].max()

# Calculate the sum of 3-point accuracy over the played seasons
sum_accuracy = players_stats_by_season_full_details['3PA'].sum()

# Calculate the average accuracy
number_of_seasons = latest_season - earliest_season + 1
average_accuracy = sum_accuracy / number_of_seasons

# Calculate the actual average number of 3-pointers made
average_3PM = players_stats_by_season_full_details['3PM'].mean()

print("Average 3-point accuracy: ", average_accuracy)
print("Actual average number of 3-pointers made: ", average_3PM)

# Make sure 'Season' is treated as a datetime object for better manipulation
players_stats_by_season_full_details['Season'] = pd.to_datetime(players_stats_by_season_full_details['Season'], format='%Y')

# Set 'Season' as the index to make it easier to interpolate
players_stats_by_season_full_details.set_index('Season', inplace=True)

# Perform linear interpolation
players_stats_by_season_full_details_interpolated = players_stats_by_season_full_details.interpolate(method='linear')

# Reset the index if you need to
players_stats_by_season_full_details_interpolated.reset_index(inplace=True)

# Now the dataframe df_interpolated has the missing values filled
print(players_stats_by_season_full_details_interpolated.loc[players_stats_by_season_full_details_interpolated['Season'].dt.year.isin([2002, 2015])])

# Calculate the required statistics for FGM
fgm_mean = players_stats_by_season_full_details['FGM'].mean()
fgm_variance = players_stats_by_season_full_details['FGM'].var()
fgm_skew = skew(players_stats_by_season_full_details['FGM'])
fgm_kurtosis = kurtosis(players_stats_by_season_full_details['FGM'])

# Calculate the required statistics for FGA
fga_mean = players_stats_by_season_full_details['FGA'].mean()
fga_variance = players_stats_by_season_full_details['FGA'].var()
fga_skew = skew(players_stats_by_season_full_details['FGA'])
fga_kurtosis = kurtosis(players_stats_by_season_full_details['FGA'])

# Print the results
print(f"FGM - Mean: {fgm_mean}, Variance: {fgm_variance}, Skew: {fgm_skew}, Kurtosis: {fgm_kurtosis}")
print(f"FGA - Mean: {fga_mean}, Variance: {fga_variance}, Skew: {fga_skew}, Kurtosis: {fga_kurtosis}")

# Extract FGM and FGA columns
FGM = players_stats_by_season_full_details['FGM']
FGA = players_stats_by_season_full_details['FGA']

# Perform relational (paired) t-test
t_stat_rel, p_value_rel = ttest_rel(FGM, FGA)

# Perform individual t-tests against a sample mean (for example, mean of FGM)
t_stat_fgm, p_value_fgm = ttest_1samp(FGM, FGM.mean())
t_stat_fga, p_value_fga = ttest_1samp(FGA, FGA.mean())

# Print the results
print(f"Paired t-test: t-statistic = {t_stat_rel}, p-value = {p_value_rel}")
print(f"Individual t-test for FGM: t-statistic = {t_stat_fgm}, p-value = {p_value_fgm}")
print(f"Individual t-test for FGA: t-statistic = {t_stat_fga}, p-value = {p_value_fga}")