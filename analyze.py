import pandas as pd

import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("learning_data.csv")
print("Raw Data:")
print(df)

# Calculate total hours per skill
total_hours = df.groupby("skill")["Hours Studied"].sum()
print("\nTotal Hours Per Skill:")
print(total_hours)

# Calculate average hours per day
df["Date"] = pd.to_datetime(df["Date"])
daily_hours = df.groupby("Date")["Hours Studied"].sum()
print("\nDaily Hours:")
print(daily_hours)



# Create a bar chart
total_hours.plot(kind="bar", color="skyblue")
plt.title("Total Hours Studied per Skill")
plt.xlabel("Skill")
plt.ylabel("Hours Studied")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()