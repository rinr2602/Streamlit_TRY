import streamlit as st
import pandas as pd
import numpy as np

st.header('Checkbox')

st.write('What would you like to eat?')

food1 = st.checkbox('Ice Cream')
food2 = st.checkbox('Coffee')
food3 = st.checkbox('Cola')

if food1:
    st.write('You chose ice cream')
elif food2:
    st.write('You chose Coffee')
elif food3:
    st.write('You chose Cola')