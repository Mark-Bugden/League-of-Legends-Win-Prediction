import streamlit as st
import requests
import random

random.seed(1)

header = st.container()
team_selection = st.container()
win_prediction = st.container()



# Load the champion information
champion_url = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion.json'
r = requests.get(champion_url)
json_data = r.json()
champion_data = json_data['data']

champions = list(champion_data.keys())



with header:
    st.title('Match Lobby Win Prediction')
    st.text('Predict the winner of a League of Legends match using only champion info')




with team_selection:
    st.header('Choose the teams ')

    columns = ["Team1selection", "Team1champs", "team2selection", "Team2champs"]

    champ_roles = ["top", "jg", "mid", "adc", "sup"]

    col21, col22, col23, col24 = st.columns(4)

    with col21:
        st.write("Choose the blue champions")

    with col22:
        st.write("# Blue")

    with col23:
        st.write("Choose the red team champions")

    with col24:
        st.write("# Red")


    rand_champs = random.sample(champions, 10)
    blue_champs = rand_champs[0:5]
    red_champs = rand_champs[5:]
    initial_blue_index = [champions.index(champ) for champ in blue_champs]
    initial_red_index = [champions.index(champ) for champ in red_champs]



    for i, col in enumerate(champ_roles):
        col21, col22, col23, col24 = st.columns(4)

        with col21:
            blue_champs[i] = st.selectbox("Blue Champion "+str(i+1), options=champions, key=col + "bluechamp" +str(i), index=initial_blue_index[i])

        with col22:
            st.image(f'img/Champion Icons/{blue_champs[i]}.png', caption=f'{blue_champs[i]}')

        with col23:
            red_champs[i] = st.selectbox("Red Champion "+str(i+1), options=champions, key=col + "redchamp" +str(i), index=initial_red_index[i])

        with col24:
            st.image(f'img/Champion Icons/{red_champs[i]}.png', caption=f'{red_champs[i]}')

with win_prediction:
    st.header('Use the Neural Network to predict the winner')
    if st.button('Calculate winner'):
        st.write('The predicted winner is: ')
        st.write('# BLUE')
        st.write('The confidence of this prediction is: HIGH')