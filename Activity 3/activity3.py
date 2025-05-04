# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:32:14 2025

@author: Administrator
"""

import streamlit as st

st.sidebar.title("Filters")
filter_value = st.sidebar.slider("Select a value", 0, 100, 50)

col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with st.expander("More Information"):
    st.write("This is extra information.")
