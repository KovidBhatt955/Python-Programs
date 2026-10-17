# Game-stats-analyser.PY
# Activity: Gaming eaderboard Analyser
# Lesson: Introduction to Pandas

import pandas as pd

# PART 1 - Create a Pandas series of top player scores
print('~~~~~~~~~~ PART 1: Pandas Series ~~~~~~~~~~')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=["GodGamer", "NormanTheGamer", "PixelKing", "GeorgeNotFound", "AJTHEBOLD"])
print(players)

# PART 2 - Create a DataFrame of gaming stats
print()
print("~~~~~~~~~~ PART 2: Pandas DataFrame ~~~~~~~~~~")
data = {
    'Player': ["GodGamer", "NormanTheGamer", "PixelKing", "GeorgeNotFound", "AJTHEBOLD"],
    'Level': [43, 41, 35, 29, 19],
    'Score': [98500, 87200, 76400, 65100, 54800],
    'Wins': [3572, 3132, 2638, 2562, 2463]
}
df = pd.DataFrame(data)
print(df)

# PART 3 - Access rows using .loc
print()
print("~~~~~~~~~~ PART 3: Accessing Rows ~~~~~~~~~~")
print("Row 0: (top player):")
print(df.loc[0])
print()
print("Rows 2 and 3:")
print(df.loc[2:3])

# PART 4 - Load Leaderboard.csv and view the data
print()
print("~~~~~~~~~~ PART 4: Reading a CSV file ~~~~~~~~~~")
full_df = pd.read_csv('leaderboard.csv')
print("First 5 rows (head):")
print(full_df.head())
print()
print("Last 3 Rows (tail):")
print(full_df.tail(3))
print()
print("Dataset info:")
print(full_df.info())

# PART 5 - Clean the data
print()
print("~~~~~~~~~~ PART 5: Cleaning Data ~~~~~~~~~~")
print("Rows with missing values removed (dropna):")
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print("Missing values filled woth 0 (fillna):")
filled_df = full_df.fillna(0)
print(filled_df.to_string())