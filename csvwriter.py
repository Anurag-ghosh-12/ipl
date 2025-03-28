import pandas as pd

data = [
    [1, "HV Patel", 24, 14, 9.18, 20.21, 13.21],
    [2, "CV Varun", 21, 14, 7.98, 19.57, 14.71],
    [3, "JJ Bumrah", 20, 13, 6.24, 17.05, 16.40],
    [4, "AD Russell", 19, 14, 9.70, 16.00, 9.89],
    [5, "Arshdeep Singh", 19, 14, 9.46, 27.05, 17.16],
    [6, "Avesh Khan", 19, 15, 9.24, 28.05, 18.21],
    [7, "Harshit Rana", 19, 11, 8.75, 20.26, 13.89],
    [8, "T Natarajan", 19, 14, 8.48, 24.68, 17.47],
    [9, "PJ Cummins", 18, 16, 9.14, 31.72, 20.83],
    [10, "YS Chahal", 18, 15, 9.08, 30.44, 20.11]
]
columns = ["Rank", "Bowler", "Wickets", "Matches", "Economy", "Bowling Avg", "Strike Rate"]

df = pd.DataFrame(data, columns=columns)
df.to_csv("bowler_stat_2024.csv", index=False)

print("CSV file saved as 'bowler_statistics.csv'")
