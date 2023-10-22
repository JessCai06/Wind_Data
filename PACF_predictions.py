from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# we want the papalote 2 power vs time
df = pd.read_csv("Wind Farm Data - All data.csv")
time_stamps = [i for i in range(0, 167)]
df = df.assign(index = time_stamps)
ma2 = np.array(time_stamps)
ar2 = np.array(df["Location 2"])

# Create ARMA process
AR2_process = ArmaProcess(ar2, ma2).generate_sample(nsample=1000)

fig, ax = plt.subplots()

ax.plot(AR2_process)
ax.set_xlabel('Timesteps')
ax.set_ylabel('Value')

# Calculate y-axis limits
y_min = np.min(AR2_process) - 10  # Adjust as needed
y_max = np.max(AR2_process) + 10  # Adjust as needed

ax.set_ylim(y_min, y_max)  # Set y-axis limits

fig.autofmt_xdate()
plt.tight_layout()

plt.show()

"""

ADF_result = adfuller(AR2_process)

print(f'ADF Statistic: {ADF_result[0]}')
print(f'p-value: {ADF_result[1]}')

plot_acf(AR2_process, lags=30);

plt.tight_layout()
# Display the figure
"""