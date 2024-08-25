import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('Global Temperature.csv')

# Streamlit app layout
st.title('Global Temperature Anomalies Dashboard')

# Sidebar for user input
st.sidebar.header('User Input Parameters')
year_range = st.sidebar.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()), (1900, 2020))

# Filter data based on the selected year range
filtered_data = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Display the filtered data
st.write(f"Displaying data from {year_range[0]} to {year_range[1]}")
st.dataframe(filtered_data)

# Visualization Selection
viz_selection = st.sidebar.selectbox('Select Visualization', ['Line Plot', 'Scatter Plot', 'Heatmap'])

# Line plot for Annual Anomalies over time
if viz_selection == 'Line Plot':
    st.subheader('Annual Temperature Anomalies Over Time')
    fig_line = px.line(filtered_data, x='Year', y='  Annual Anomaly', title='Annual Temperature Anomalies Over Time')
    st.plotly_chart(fig_line)

    st.subheader('Five-Year vs Ten-Year Temperature Anomaly')
    fig_line_compare = px.line(filtered_data, x='Year', y=[' Five-Year Anomaly', ' Ten-Year Anomaly'], 
                               labels={'value': 'Temperature Anomaly'}, title='Five-Year vs Ten-Year Anomaly')
    st.plotly_chart(fig_line_compare)

# Scatter plot for Monthly Anomaly vs Monthly Uncertainty
elif viz_selection == 'Scatter Plot':
    st.subheader('Monthly Anomaly vs Monthly Uncertainty')
    fig_scatter = px.scatter(filtered_data, x='Monthly Anomaly', y=' Monthly Unc.',
                             title='Monthly Anomaly vs Monthly Uncertainty')
    st.plotly_chart(fig_scatter)

# Heatmap for Correlation Matrix
elif viz_selection == 'Heatmap':
    st.subheader('Correlation Matrix of Temperature Anomalies')
    corr_matrix = filtered_data.corr()
    fig_heatmap = px.imshow(corr_matrix, title='Correlation Matrix')
    st.plotly_chart(fig_heatmap)

# Additional visualization
st.subheader('Distribution of Annual Temperature Anomalies')
fig_hist = px.histogram(filtered_data, x='Annual Anomaly', nbins=20, title='Distribution of Annual Temperature Anomalies')
st.plotly_chart(fig_hist)
