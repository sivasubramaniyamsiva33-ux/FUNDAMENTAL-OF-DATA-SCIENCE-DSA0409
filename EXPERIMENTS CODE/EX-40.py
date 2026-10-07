"""
Exercise 40: Soccer Player Analysis using Pandas
Key Idea: nlargest() finds top players and value_counts() gives position frequencies.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Create and save the dataset
data = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F", "G"],
    "Age": [22, 25, 28, 24, 30, 27, 23],
    "Position": ["Forward", "Midfielder", "Forward", "Defender", "Goalkeeper", "Forward", "Defender"],
    "Goals": [15, 8, 20, 4, 1, 12, 5],
    "Salary": [5000, 4500, 7000, 3500, 4000, 6000, 3800]
})
data.to_csv("soccer_players.csv", index=False)

# Read CSV
players = pd.read_csv("soccer_players.csv")

print("Top 5 goal scorers:")
print(players.nlargest(5, "Goals")[["Name", "Goals"]])

print("Top 5 salaries:")
print(players.nlargest(5, "Salary")[["Name", "Salary"]])

average_age = players["Age"].mean()
print("Average age =", average_age)

print("Players above average age:")
print(players[players["Age"] > average_age]["Name"])

players["Position"].value_counts().plot(kind="bar")
plt.title("Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()
