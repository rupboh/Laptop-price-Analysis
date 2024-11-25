import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Cleaned.csv")

# Title and description
st.title("Price Analysis Dashboard")
st.markdown("Explore the variation of Price with other columns in the dataset")

# Columns for the plots
col1, col2 = st.columns(2, gap="small")

# Sidebar for column selection
cat_cols = ['Company', 'TypeName', 'Cpu', 'Gpu', 'OpSys']
num_cols = ['Ram', 'Weight', 'Touchscreen', 'IPS', 'ppi']
all_cols = cat_cols + num_cols

selected_col = st.sidebar.selectbox("Select a column to compare", all_cols)

if selected_col:
    if selected_col in cat_cols:
        # For categorical columns
        with col1:
            st.header("Box Plot")
            box_fig = px.box(df, x=selected_col, y='Price', title=f'Price Distribution by {selected_col}')
            st.plotly_chart(box_fig, use_container_width=True)

        with col2:
            st.header("Bar Graph")
            bar_fig = px.bar(df, x=selected_col, y='Price', title=f'Price Variation by {selected_col}')
            st.plotly_chart(bar_fig, use_container_width=True)

    else:
        # For numeric columns
        with col1:
            st.header("Box Plot")
            box_fig = px.box(df, x=selected_col, y='Price', title=f'Price Distribution by {selected_col}')
            st.plotly_chart(box_fig, use_container_width=True)

        with col2:
            st.header("Scatter Plot")
            scatter_fig = px.scatter(df, x=selected_col, y='Price', trendline='ols', title=f'Price vs {selected_col}')
            st.plotly_chart(scatter_fig, use_container_width=True)
