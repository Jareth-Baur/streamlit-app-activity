# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:19:24 2025
@author: Administrator
"""

import streamlit as st
import pandas as pd

st.title("📊 DataFrame Viewer")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        if data.shape[1] < 5:
            st.error("The uploaded file must contain at least 5 columns.")
        else:
            st.success("File uploaded successfully!")

            # Toggle raw data display
            if st.checkbox("Show raw data"):
                st.subheader("Raw Data")
                st.dataframe(data)

            # Column filter selection
            selected_column = st.selectbox("Select a column to filter by", data.columns)
            unique_values = data[selected_column].dropna().unique()

            selected_value = st.selectbox(f"Filter rows where `{selected_column}` is:", sorted(unique_values.astype(str)))

            filtered_data = data[data[selected_column].astype(str) == selected_value]

            st.subheader(f"Filtered Data (where `{selected_column}` = {selected_value})")
            st.dataframe(filtered_data)

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Please upload a CSV file to begin.")
