import pandas as pd
import json

# Load your dataset
df = pd.read_csv("cricket.csv")

# Get unique teams (from both team and opponent columns)
teams = sorted(set(df["team"]).union(df["opponent"]))

# Get unique grounds
grounds = sorted(df["ground"].unique())

# Save to JSON
with open("teams.json", "w") as f:
    json.dump(teams, f, indent=2)

with open("grounds.json", "w") as f:
    json.dump(grounds, f, indent=2)

print("✅ JSON files created: teams.json, grounds.json")
