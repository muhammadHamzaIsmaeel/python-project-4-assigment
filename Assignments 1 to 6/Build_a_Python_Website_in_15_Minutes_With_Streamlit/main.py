import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Analysis App")

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Overview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter", columns)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox("Select a value to filter by", unique_values)

    filtered_df = df[df[selected_column] == selected_values]
    st.write(filtered_df)

    st.subheader("Data Visualization")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Please upload a CSV file to get started.")        