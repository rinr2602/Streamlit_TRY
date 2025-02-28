import streamlit as st
st.set_page_config(layout = 'wide')

st.title('How to configure the layout for your app')

with st.expander('About this app:'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
username = st.sidebar.text_input('What is your name?')
useremoji = st.sidebar.selectbox(
    'What are you feeling?',
    ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
userfood = st.sidebar.selectbox(
    'What do you feel like eating?',
    ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza']
)    

st.header('Output')

col1, col2, col3 = st.columns(3)
with col1:
    if username != '':
        st.write('Hey, {}'.format(username))
    else:
        st.write('Hey, write your name please!')

with col2:
    if useremoji != '':
        st.write("Ah, you're feeling {}".format(useremoji))
    else:
        st.write("Choose what you're feeling please!")

with col3:
    if userfood != '':
        st.write('{} is a nice choice!'.format(userfood))
    else:
        st.write("You don't feel like eating anything?")