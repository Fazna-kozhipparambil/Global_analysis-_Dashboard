# -*- coding: utf-8 -*-
"""Global_Temperature_Visualization_Dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Fazna-kozhipparambil/Global-Temperature-analysis/blob/main/Global_Temperature_Visualization_Dashboard.ipynb
"""

import pandas as pd

# Load the CSV file from the uploaded location
df = pd.read_csv('Global Temperature.csv')
 # Display the first few rows of the dataframe
df.head()

# Display column names
print(df.columns)

"""**Create Simple Visualization**

1. Line Plot of Annual Anomalies

Let's plot the Year against the Annual Anomaly to see how the anomaly changes over time.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Plotting the Annual Anomaly over the years
plt.figure(figsize=(12, 6))

# Plotting the Annual Anomaly over the years
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='  Annual Anomaly', data=df)
plt.title('Annual Temperature Anomaly Over Time')
plt.xlabel('Year')
plt.ylabel('Annual Anomaly')
# Remove y-axis tick marks and labels
ax = plt.gca()  # Get the current axis
ax.yaxis.set_ticks([])  # Remove tick marks
plt.show()



"""
2. Line Plot of Monthly Anomalies"""

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Monthly Anomaly', data=df)
plt.title('Monthly Temperature Anomaly Over Time')
plt.xlabel('Year')
plt.ylabel('Monthly Anomaly')
plt.show()

"""
3. Plotting Five-Year and Ten-Year Anomalies Together

You can compare the Five-Year Anomaly and Ten-Year Anomaly in the same plot:"""

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Five-Year Anomaly', data=df, label='Five-Year Anomaly')
sns.lineplot(x='Year', y=' Ten-Year Anomaly', data=df, label='Ten-Year Anomaly')
plt.title('Five-Year vs Ten-Year Temperature Anomaly')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
# Remove y-axis tick marks and labels
ax = plt.gca()  # Get the current axis
ax.yaxis.set_ticks([])  # Remove tick marks
plt.legend()
plt.show()

"""4. Scatter Plot with Monthly Anomaly and Uncertainty

To visualize the relationship between the Monthly Anomaly and Monthly Unc.:

"""

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Monthly Anomaly', y=' Monthly Unc.', data=df)
plt.title('Monthly Anomaly vs Monthly Uncertainty')
plt.xlabel('Monthly Anomaly')
plt.ylabel('Monthly Uncertainty')
# Remove y-axis tick marks and labels
ax = plt.gca()  # Get the current axis
ax.yaxis.set_ticks([])  # Remove tick marks

plt.show()

"""5. Visualization of Multiple Anomalies Together

"""

plt.figure(figsize=(14, 8))

sns.lineplot(x='Year', y='  Annual Anomaly', data=df, label='Annual Anomaly')
sns.lineplot(x='Year', y='Five-Year Anomaly', data=df, label='Five-Year Anomaly')
sns.lineplot(x='Year', y=' Ten-Year Anomaly', data=df, label='Ten-Year Anomaly')
sns.lineplot(x='Year', y='  Twenty-Year Anomaly', data=df, label='Twenty-Year Anomaly')

# Titles and labels
plt.title('Temperature Anomalies Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly', fontsize=12)


# Remove y-axis tick marks and labels
ax = plt.gca()  # Get the current axis
ax.yaxis.set_ticks([])  # Remove tick marks


plt.legend()
plt.show()

"""**Analysis**

1. Correlation Analysis
Objective: Understand the relationships between different anomaly metrics (e.g., Annual Anomaly, Five-Year Anomaly, etc.).

Method: Use a correlation matrix with a heatmap to visualize how different anomaly measurements relate to each other.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Compute the correlation matrix
corr = df.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Temperature Anomalies')
plt.show()

"""2. Moving Averages
Objective: Smooth out the data to identify long-term trends.

Method: Calculate moving averages for temperature anomalies over different periods (e.g., 5-year, 10-year).
"""

df['5-Year MA'] = df['  Annual Anomaly'].rolling(window=5).mean()
df['10-Year MA'] = df['  Annual Anomaly'].rolling(window=10).mean()

# Plotting
plt.figure(figsize=(14, 8))
sns.lineplot(x='Year', y='  Annual Anomaly', data=df, label='Annual Anomaly')
sns.lineplot(x='Year', y='5-Year MA', data=df, label='5-Year Moving Average')
sns.lineplot(x='Year', y='10-Year MA', data=df, label='10-Year Moving Average')
plt.title('Annual Anomaly and Moving Averages Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
# Remove y-axis tick marks and labels
ax = plt.gca()  # Get the current axis
ax.yaxis.set_ticks([])  # Remove tick marks
plt.legend()
plt.show()

# Drop rows with any missing values
df_cleaned = df.dropna()

##Forward Fill: Fills missing values with the last known value.
df_filled = df.fillna(method='ffill')

#Backward Fill: Fills missing values with the next known value.
df_filled = df.fillna(method='bfill')

#Interpolation: Interpolates missing values based on the data trend.
df_filled = df.interpolate(method='linear')

import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Fill missing values by linear interpolation
df_filled = df.interpolate(method='linear')

# Ensure no missing values remain
print(df_filled.isnull().sum())

# Convert to numeric if necessary
df_filled['  Annual Anomaly'] = pd.to_numeric(df_filled['  Annual Anomaly'], errors='coerce')

# Smoothing the data if necessary
df_smoothed = df_filled['  Annual Anomaly'].rolling(window=3, min_periods=1).mean()

# Perform seasonal decomposition with adjusted period
result = seasonal_decompose(df_smoothed, model='additive', period=12)

# Plot the components
result.plot()
plt.show()

"""3.Anomaly Detection
Objective: Identify years that had unusually high or low temperature anomalies.

Method: Use z-scores or other statistical methods to detect outliers.
"""

import pandas as pd
import numpy as np
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

# Check for the presence and type of columns
if '  Annual Anomaly' not in df.columns or 'Year' not in df.columns:
    raise ValueError("Columns '  Annual Anomaly' or 'Year' are missing from the DataFrame")

# Ensure the data types are numeric
df['  Annual Anomaly'] = pd.to_numeric(df['  Annual Anomaly'], errors='coerce')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Drop rows with missing values in 'Annual Anomaly' or 'Year'
df = df.dropna(subset=['  Annual Anomaly', 'Year'])

# Calculate z-scores of the 'Annual Anomaly' column
df['z_score'] = zscore(df['  Annual Anomaly'])

# Identify anomalies (adjust the threshold as needed)
anomalies = df[df['z_score'].abs() > 2]

# Plot the data and highlight anomalies
plt.figure(figsize=(14, 8))
sns.lineplot(x='Year', y='  Annual Anomaly', data=df, label='Annual Anomaly')
plt.scatter(anomalies['Year'], anomalies['  Annual Anomaly'], color='red', label='Anomalies')
plt.title('Temperature Anomalies with Detected Outliers')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.legend()
plt.show()

"""4. Trend Analysis
Objective: Determine the long-term trend in temperature anomalies.

Method: Fit a linear regression model to the data to quantify the trend.
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Prepare the data for linear regression
X = df['Year'].values.reshape(-1, 1)
y = df['  Annual Anomaly'].values

# Create and fit the model
model = LinearRegression()
model.fit(X, y)
trend = model.predict(X)

# Plotting
plt.figure(figsize=(14, 8))
sns.lineplot(x='Year', y='  Annual Anomaly', data=df, label='Annual Anomaly')
plt.plot(df['Year'], trend, color='red', label='Trend')
plt.title('Temperature Anomaly Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.legend()
plt.show()

"""5. Hypothesis Testing
Objective: Test hypotheses related to temperature anomalies, such as whether anomalies have significantly increased in the last century.

Method: Use statistical tests like t-tests, chi-square tests, etc.
"""

import pandas as pd
from scipy.stats import ttest_ind

# Sample DataFrame for demonstration
# df = pd.read_csv('your_data.csv')

# Ensure 'Annual Anomaly' and 'Year' are numeric
df['  Annual Anomaly'] = pd.to_numeric(df['  Annual Anomaly'], errors='coerce')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Drop rows with missing values in 'Annual Anomaly' or 'Year'
df = df.dropna(subset=['  Annual Anomaly', 'Year'])

# Split data into two periods
df_pre_1950 = df[df['Year'] < 1950]['  Annual Anomaly']
df_post_1950 = df[df['Year'] >= 1950]['  Annual Anomaly']

# Ensure there are no empty arrays
if df_pre_1950.empty or df_post_1950.empty:
    raise ValueError("One of the data periods is empty. Check the data filtering.")

# Perform a t-test
t_stat, p_val = ttest_ind(df_pre_1950, df_post_1950, nan_policy='omit')

print(f"T-statistic: {t_stat}, P-value: {p_val}")

"""Statistical Significance: Given that the p-value is extremely small (much less than common significance levels like 0.05 or 0.01), you can conclude that there is a statistically significant difference between the temperature anomalies before and after 1950.

Effect Size: The large magnitude of the t-statistic suggests a substantial difference between the two periods, indicating that the temperature anomalies have changed significantly over time.

**Interactive Dashboard**
1. Set Up Your Environment in Colab
"""

"""2. Write  Streamlit App Code"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# 
# # Load the dataset
# df = pd.read_csv('/content/Global Temperature.csv')
# 
# # Streamlit app layout
# st.title('Global Temperature Anomalies Dashboard')
# 
# # Year range slider
# year_range = st.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()), (1900, 2020))
# 
# # Filter data based on the selected year range
# filtered_data = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
# 
# # Display the filtered data
# st.write(f"Displaying data from {year_range[0]} to {year_range[1]}")
# st.dataframe(filtered_data)
# 
# # Line plot for Annual Anomalies over time
# fig_line = px.line(filtered_data, x='Year', y='Annual Anomaly',
#                    title='Annual Temperature Anomalies Over Time')
# st.plotly_chart(fig_line)
# 
# # Histogram of anomalies
# fig_hist = px.histogram(filtered_data, x='Annual Anomaly',
#                         nbins=20, title='Distribution of Annual Temperature Anomalies')
# st.plotly_chart(fig_hist)
#

"""3. Run Your Streamlit App Using Ngrok"""

# Run the Streamlit app

# Expose the app to the web using ngrok
public_url = ngrok.connect(port='8501')
public_url
