import pandas as pd

df = pd.read_csv("filtered_dataset.csv")
df.head()

name = df["star_name"].to_list()
mass = df["mass"].to_list()
radius = df["radius"].to_list()
dist = df["distance"].to_list()
gravity = df["gravity"].to_list()
print("dictionary work")

final_final = []

final_final = []
for i in range(len(name)):
    temp = {
        'name': name[i],
        'mass': mass[i],
        'radius': radius[i],
        'distance': dist[i],
        'gravity': gravity[i]
    }
    final_final.append(temp)
print(final_final)

final_star_list = df.to_dict(orient='records')
print("working")
print(final_star_list)
