import numpy as np
import os

# Get the file path relative to the current script's directory
file_path = os.path.join(os.path.dirname(__file__), 'NBA_Player_Stats.tsv')

# Load the data using the dynamic file path
data = np.genfromtxt(file_path, delimiter='\t', dtype=None, encoding=None, names=True)

# Extract relevant columns using the provided column names
players = data['Player']
seasons = data['Season']
games_played = data['GP'].astype(float)
minutes_played = data['MIN'].astype(float)
field_goals_made = data['FGM'].astype(float)
field_goals_attempted = data['FGA'].astype(float)
three_points_made = data['3PM'].astype(float)
three_points_attempted = data['3PA'].astype(float)
free_throws_made = data['FTM'].astype(float)
free_throws_attempted = data['FTA'].astype(float)
points = data['PTS'].astype(float)
blocks = data['BLK'].astype(float)
steals = data['STL'].astype(float)

# Calculate metrics
field_goal_accuracy = np.divide(field_goals_made, field_goals_attempted, out=np.zeros_like(field_goals_made), where=field_goals_attempted!=0)
three_point_accuracy = np.divide(three_points_made, three_points_attempted, out=np.zeros_like(three_points_made), where=three_points_attempted!=0)
free_throw_accuracy = np.divide(free_throws_made, free_throws_attempted, out=np.zeros_like(free_throws_made), where=free_throws_attempted!=0)
points_per_minute = np.divide(points, minutes_played, out=np.zeros_like(points), where=minutes_played!=0)
overall_shooting_accuracy = np.divide(field_goals_made + three_points_made + free_throws_made, field_goals_attempted + three_points_attempted + free_throws_attempted, out=np.zeros_like(field_goals_made), where=(field_goals_attempted + three_points_attempted + free_throws_attempted)!=0)
blocks_per_game = np.divide(blocks, games_played, out=np.zeros_like(blocks), where=games_played!=0)
steals_per_game = np.divide(steals, games_played, out=np.zeros_like(steals), where=games_played!=0)

# Display the calculated metrics
for i in range(len(players)):
    print(f"Player: {players[i]}, Season: {seasons[i]}")
    print(f"Field Goal Accuracy: {field_goal_accuracy[i]:.2f}")
    print(f"Three Point Accuracy: {three_point_accuracy[i]:.2f}")
    print(f"Free Throw Accuracy: {free_throw_accuracy[i]:.2f}")
    print(f"Points Per Minute: {points_per_minute[i]:.2f}")
    print(f"Overall Shooting Accuracy: {overall_shooting_accuracy[i]:.2f}")
    print(f"Blocks Per Game: {blocks_per_game[i]:.2f}")
    print(f"Steals Per Game: {steals_per_game[i]:.2f}")
    print()
