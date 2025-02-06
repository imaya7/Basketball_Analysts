import numpy as np
import os

# Load the data
file_path = os.path.join(os.path.dirname(__file__), 'NBA_Player_Stats.tsv')  # Dynamically generate the file path
data = []

with open(file_path, 'r') as file:
    lines = file.readlines()
    headers = lines[0].strip().split('\t')
    for line in lines[1:]:
        values = line.strip().split('\t')
        data.append(dict(zip(headers, values)))

# Convert relevant columns to NumPy arrays
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return 0

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0

# Extract relevant columns and handle missing values
FGM = np.array([safe_int(row['FGM']) for row in data])
FGA = np.array([safe_int(row['FGA']) for row in data])
TPM = np.array([safe_int(row['3PM']) for row in data])
TPA = np.array([safe_int(row['3PA']) for row in data])
FTM = np.array([safe_int(row['FTM']) for row in data])
FTA = np.array([safe_int(row['FTA']) for row in data])
PTS = np.array([safe_int(row['PTS']) for row in data])
MIN = np.array([safe_float(row['MIN']) for row in data])
BLK = np.array([safe_int(row['BLK']) for row in data])
STL = np.array([safe_int(row['STL']) for row in data])
GP = np.array([safe_int(row['GP']) for row in data])

# Calculate the metrics using NumPy
field_goal_accuracy = np.divide(FGM, FGA, out=np.zeros_like(FGM, dtype=float), where=FGA != 0)
three_point_accuracy = np.divide(TPM, TPA, out=np.zeros_like(TPM, dtype=float), where=TPA != 0)
free_throw_accuracy = np.divide(FTM, FTA, out=np.zeros_like(FTM, dtype=float), where=FTA != 0)
average_points_per_minute = np.divide(PTS, MIN, out=np.zeros_like(PTS, dtype=float), where=MIN != 0)
overall_shooting_accuracy = np.divide((FGM + TPM + FTM), (FGA + TPA + FTA), out=np.zeros_like(FGM, dtype=float), where=(FGA + TPA + FTA) != 0)
average_blocks_per_game = np.divide(BLK, GP, out=np.zeros_like(BLK, dtype=float), where=GP != 0)
average_steals_per_game = np.divide(STL, GP, out=np.zeros_like(STL, dtype=float), where=GP != 0)

# Calculate average points per game (PPG)
average_points_per_game = np.divide(PTS, GP, out=np.zeros_like(PTS, dtype=float), where=GP != 0)

# Add the calculated metrics to the data
for i, row in enumerate(data):
    row['field_goal_accuracy'] = field_goal_accuracy[i]
    row['three_point_accuracy'] = three_point_accuracy[i]
    row['free_throw_accuracy'] = free_throw_accuracy[i]
    row['average_points_per_minute'] = average_points_per_minute[i]
    row['overall_shooting_accuracy'] = overall_shooting_accuracy[i]
    row['average_blocks_per_game'] = average_blocks_per_game[i]
    row['average_steals_per_game'] = average_steals_per_game[i]
    row['average_points_per_game'] = average_points_per_game[i]

# Function to get top 100 players for a given metric
def get_top_100_players(metric):
    sorted_data = sorted(data, key=lambda x: x[metric], reverse=True)
    return sorted_data[:100]

# Create lists of top 100 players for each metric
top_100_field_goal_accuracy = get_top_100_players('field_goal_accuracy')
top_100_three_point_accuracy = get_top_100_players('three_point_accuracy')
top_100_free_throw_accuracy = get_top_100_players('free_throw_accuracy')
top_100_average_points_per_minute = get_top_100_players('average_points_per_minute')
top_100_overall_shooting_accuracy = get_top_100_players('overall_shooting_accuracy')
top_100_average_blocks_per_game = get_top_100_players('average_blocks_per_game')
top_100_average_steals_per_game = get_top_100_players('average_steals_per_game')
top_100_average_points_per_game = get_top_100_players('average_points_per_game')  # New top 100 for PPG

# Print the results
def print_top_100(metric, top_100):
    print(f"Top 100 {metric.replace('_', ' ').title()}:")
    for player in top_100:
        print(f"{player['Player']} ({player['Season']}): {player[metric]:.3f}")
    print("\n")

# Display the top 100 players for each metric
print_top_100('field_goal_accuracy', top_100_field_goal_accuracy)
print_top_100('three_point_accuracy', top_100_three_point_accuracy)
print_top_100('free_throw_accuracy', top_100_free_throw_accuracy)
print_top_100('average_points_per_minute', top_100_average_points_per_minute)
print_top_100('overall_shooting_accuracy', top_100_overall_shooting_accuracy)
print_top_100('average_blocks_per_game', top_100_average_blocks_per_game)
print_top_100('average_steals_per_game', top_100_average_steals_per_game)
print_top_100('average_points_per_game', top_100_average_points_per_game)  # Print top 100 PPG
