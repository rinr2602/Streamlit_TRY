import streamlit as st
import pandas as pd
import numpy as np

st.header('Multiselect')

options = st.multiselect(
    'What are your fave colours?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected: ', options)