import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
data = pd.read_csv('istherecorrelation.csv', delimiter=';')
data['WO [x1000]'] = data['WO [x1000]'].str.replace(',', '.').astype(float)

# Creating the figure and the first axis (for WO)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting WO on the first y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color='blue')
ax1.plot(data['Year'], data['WO [x1000]'], label='WO [x1000]', color='blue', marker='o')
ax1.tick_params(axis='y', labelcolor='blue')

# Setting a y-axis range for WO
ax1.set_ylim([200, 300])  

# Creating a second y-axis for NL Beer consumption
ax2 = ax1.twinx()  
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='green')
ax2.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], label='NL Beer Consumption', color='green', marker='o')
ax2.tick_params(axis='y', labelcolor='green')

# Setting a y-axis range for NL Beer consumption
ax2.set_ylim([11000, 12500])  

# Showing the plot
plt.title('WO and NL Beer Consumption Over the Years')
fig.tight_layout()  
plt.savefig('wo_beer.png', dpi=300)
plt.show()

