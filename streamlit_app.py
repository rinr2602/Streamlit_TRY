import streamlit as st
import pandas as pd
import numpy as np

st.header('Selection Box')

option = st.selectbox(
    'What is your fave colour?',
    ('Blue','Red','Pink')
)

st.write('You have chosen: ', option)