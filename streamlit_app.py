import streamlit as st
st.set_page_config(layout = 'wide')

st.title('Bleh, Interface here')

with st.expander('About this:'):
    st.write('Just some shit here? man idk put your details dw it doesnt get stored for me lol')
    st.write('dummy image below btw')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
username = st.sidebar.text_input('Who is you?')
useremoji = st.sidebar.selectbox(
    'How you doin?',
    ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
userfood = st.sidebar.selectbox(
    'What do you eat when you feel like doing big back activities?',
    ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza']
)    

st.header('Output')

col1, col2, col3 = st.columns(3)
with col1:
    if username != '':
        st.write('Hey, {}'.format(username))
    else:
        st.write('Write your name bruh??')

with col2:
    if useremoji != '':
        st.write("Ah, you're feeling {}".format(useremoji))
    else:
        st.write("Choose what youre feeling, dont be that 'emotions are for the weak alpha sigma chad type'")

with col3:
    if userfood != '':
        st.write('{}, uh. prime big back activities'.format(userfood))
    else:
        st.write("Stop lying about your big back-ness")

st.write('in case you didnt figure it out, there is an arrow on the top left')