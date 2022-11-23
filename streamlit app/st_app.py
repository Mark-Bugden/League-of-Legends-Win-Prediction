import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Welcome to my awesome project')

with dataset:
    st.header('League of Legends Win Prediction')
    st.text('In this project I try to predict the winner of a League of Legends match using only the team composition')



with features:
    st.header('Features')

with model_training:
    st.header('Model training')