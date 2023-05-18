#!/usr/bin/env python
# coding: utf-8

# Q1. What is the distinction between a numpy array and a pandas data frame? Is there a way to convert between the two if there is?
# 

# A NumPy array is a grid of values, while a Pandas DataFrame is a labeled two-dimensional structure. NumPy arrays are used for numerical computations, while DataFrames are designed for data manipulation and analysis.
# 
# 
# To convert a NumPy array to a DataFrame: pd.DataFrame(numpy_array)
# 
# To convert a DataFrame to a NumPy array: data_frame.values

# Q2. What can go wrong when an user enters in a stock-ticker symbol, and how do you handle it?

# Invalid symbol: Check if the symbol exists and is valid.
# Ambiguity: Handle cases where a symbol refers to multiple entities.
# Delisting or inactivity: Notify the user if the symbol is no longer active.
# Data availability: Inform users about limited or unavailable data.
# Retrieval errors: Handle network/API errors and provide feedback to the user.

# Q3. Identify some of the plotting techniques that are used to produce a stock-market chart.
# 

# Line Chart: Shows the closing prices over time.
# Candlestick Chart: Displays open, high, low, and close prices.
# OHLC Chart: Represents prices using vertical lines with open, high, low, and close levels.
# Volume Chart: Depicts trading volume as vertical bars.
# Moving Averages: Smooths out price fluctuations to identify trends.
# Bollinger Bands: Shows price volatility and potential reversal points.
# Relative Strength Index (RSI): Measures overbought and oversold conditions.
# MACD (Moving Average Convergence Divergence): Identifies trend signals.

# Q4. Why is it essential to print a legend on a stock market chart?
# 

# Printing a legend on a stock market chart is essential because it helps viewers understand the meaning of different elements in the chart, identify series, provide context, cross-reference data, and serve as documentation for future reference.

# Q5. What is the best way to limit the length of a pandas data frame to less than a year?
# 

# #Ensure the DataFrame has a date column.
# #Set the date column as the index.
# #Filter the DataFrame using a start and end date

# Q6. What is the definition of a 180-day moving average?

# In[47]:


import pandas as pd

data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
data_df = pd.DataFrame({'value': data})
moving_average = data_df['value'].rolling(window=180).mean()
print(moving_average)


# Q7. Did the chapter's final example use "indirect" importing? If so, how exactly do you do it?
# 

# No, the chapter's final example did not use "indirect" importing. "Indirect" importing refers to importing modules or functions using alternative names or assigning them to different variables. The example used standard import statements to directly import the required modules without any aliases or alternative names.

# In[ ]:




