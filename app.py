import streamlit as st
from pymongo import MongoClient
import random
st.set_page_config(page_title="Awara Logon", page_icon="🍕")

st.title('Agaye Awara Logon')
st.caption('Where are we eating today?')

password=st.text_input('Password', type='password')
if password != st.secrets['APP_PASS']:
    st.stop()

client=MongoClient(st.secrets['MONGO_URL'])
db=client['Restaurant']
collection=db['pick']

name=st.text_input('Enter a Restaurant')

if st.button('Save Restaurant'):
    if name.strip():
        collection.insert_one({"Place": name.strip()})
        st.success(f'"{name}" has been saved!')
    else:
        st.warning('Please enter a restaurant name')

if st.button('Suggest Restaurant'):
    restaurants=list(collection.find())
    if restaurants:
        suggestion=random.choice(restaurants)
        st.info(f"Todays restaurant suggestion is: **{suggestion['Place']}**")
    else:
        st.error('No restaurant found')