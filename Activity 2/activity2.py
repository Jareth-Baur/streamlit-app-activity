# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:19:24 2025

@author: Administrator
"""

import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("sample", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    show_raw = st.checkbox("Show raw data")
    if show_raw:
        st.dataframe(data)
    else:
        # Add data manipulation/filtering here if needed (using st.selectbox etc.)
        st.write("Summary or filtered data would go here.")
