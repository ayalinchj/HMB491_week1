import pandas as pd
import matplotlib.pyplot as plt

# TODO: load the dataset as pandas dataframe
df_teeth = pd.read_csv("mammal_teeth.csv")

plt.figure(figsize=(15, 15)) # set figure size
plt.scatter(x=df_teeth['Top incisors'],
            y=df_teeth['MAMMAL']) # set figure x, y axis
plt.gca().xaxis.set_visible(True)
# TODO: change the title name to include your name
plt.title("Top Incisors Count Across Mammal Species – Ayalinch Jonathan")
plt.savefig("mammal_teeth_scatterplot.png", dpi=150) # save the figure