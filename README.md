# Basketball_Analysts

# Purpose 
The  purpose of this assignment is to learn about the numpy python library. This project uses data on basketball players and their stats over multiple seasons. 

# Objectives 
The project determines the following: 
- the field goal accuracy, three-point accuracy, and free throw accuracy for each player in each season.
-  the average points scored per minute for each player in each season.
-  the overall shooting accuracy of each player in each season.
- the average number of blocks per game and the average number of steals per game for each player in each season

# Libraries 
- numpy (np)
- os

# Data Files 
- NBA_Column_Names.txt
- NBA_Player_Stats.tsv

# Python Files 
- All_Basketball_Players - calculates the objectives for all players 
- Top_100_Basketball - Calculates the top 100 basketball player objectives
- Note * Top_100_Basketball_players includes average points scored per game 

#  Short explanation All_Basketball_Players 
This project is designed to analyze player statistics using numpy to complete the objectives for all players, and then print the result in the terminal. 

no classes are defined 

Key Attributes 
- players: A numpy array containing the names of the players.
- seasons: A numpy array containing the seasons of the player data.
- games_played (GP): A numpy array containing the number of games played by each player.
- minutes_played (MIN): A numpy array containing the total minutes played by each player.

Methods 
- field_goal_accuracy: Calculates the percentage of field goals made (FGM / FGA).
- three_point_accuracy: Calculates the percentage of three-pointers made (3PM / 3PA).
- free_throw_accuracy: Calculates the percentage of free throws made (FTM / FTA).

Limitations 
- No class structure 
- Not much error handling 

# Short explanation Top_100_Basketball
 This project is designed to analyze and rank the players based on statistical performance throughout the different seasons. The script loads the data and then completes all the objectives for the top-rank 100 players and then prints the result 
 
no defined classes 

Attributes 
- data: A list of dictionaries where each dictionary represents a player and contains their statistical data for a given season

Methods 
- safe_int(value): Converts a value to an integer, returning 0 if the conversion fails 
- This is for incidents of missing or improperly formed data 
- safe_float(value): Converts a value to a float, returning 0.0 if the conversion fails.
- Metric Calculation: The code computes various metrics using NumPy

limitations 
- Slow performance 
- fixed to the top 100 players 

# Why two different Python files 
I did try to combine them into one file but I just kept getting errors so I made two different files. Also having two different files keeps the terminals from being clustered with a lot of data. 

