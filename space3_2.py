import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
import io 


URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
resp = urllib.request.urlopen(URL)
data__ = resp.read() # Decode the response as UTF-8 text
dataset_part_2_csv = io.BytesIO(data__)
df=pd.read_csv(dataset_part_2_csv)
sns.catplot(y="Orbit", x="Outcome", hue="Class", data=df, aspect = 5)
plt.xlabel("Outcome",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.figure(figsize=(10, 6))  # Optional: set the figure size
outcome_counts = df['Outcome'].value_counts()
plt.bar(outcome_counts.index, outcome_counts.values)

# Optional: Customize the bar chart
plt.xlabel("Outcome", fontsize=20)
plt.ylabel("Orbit", fontsize=20)
plt.title("Scatter Plot: Flight Number vs. Orbit (Colored by Class)", fontsize=16)

plt.show()

year=[]
def Extract_year():
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year
Extract_year()
df['Date'] = year
df.head()
features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()
    