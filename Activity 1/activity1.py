# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:00:49 2025

@author: Administrator
"""

import streamlit as st

st.title("Hello, Streamlit!")
st.header("This is a header.")
st.write("This is some text.")

name = st.text_input("Enter your name:")
number = st.number_input("Enter a number:")

st.write(f"Hello, {name}! You entered the number: {number}")
