# -*- coding: utf-8 -*-
"""
Created on Wed September 22 11:13:28 2021

@author: Dilini
"""
from pycaret.regression import *
import streamlit as st
import pandas as pd
import numpy as np


def run():
    model = load_model('Final_ET_Model_22Sep2021')

    def predict(model, input_df):
        predictions_df = predict_model(estimator=model, data=input_df)
        predictions = predictions_df['Label'][0]
        return predictions

    st.title("Recommendation predictions")
    st.markdown("")
    st.markdown("")

    st.info('Move the sliders and click Predict')

    var2 = st.selectbox(
        'What is your age group?',
        ("Under 15",
         "15-17",
         "18-20",
         "21-25",
         "21-25",
         "26-30",
         "31-35",
         "36-40",
         "41 and older"))

    var4O13 = st.selectbox('Do you watch traditional sports on TV or online, eg. football, rugby, tennis? No = 0; Yes = 1', ("Yes", 'No'))

    var31 = st.selectbox(
        'Which of the following is your most preferred football videogame?',
        ("FIFA Soccer / EA FIFA Mobile",
         "eFootball PES",
         "Mini Football",
         'Dream League Soccer',
         'Football Cup',
         'Stickman Soccer',
         'Top Eleven 2021',
         'Football Manager 2021',
         'Season Pro Football Manager',
         'Online Soccer Manager',
         'PES Club Manager',
         'Head Ball 2',
         'Soccer Stars',
         'Soccer Royale',
         'Puppet Soccer Champions League',
         'Real Juggle',
         'Score!Hero (1 or2)',
         'Rumble Stars',
         'Football Strike'))

    st.markdown("")
    st.markdown("")
    st.markdown("")
    var32 = st.slider(
        'How interested are you personally in real football? -1 = Not at all; 100 = Extremely',
        -1.0, 100.0, 50.0, 1.0)

    var35 = st.slider(
        'How would you rate your own skill playing game you selected above? -1 = Very low; 100 = Very high',
        -1.0, 100.0, 50.0, 1.0)

    var37O256 = st.slider(
        'How realistic and accurate is the gameplay environment of your favourite game above? -1 = Not realistic; 100 = Extremely realistic',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("***")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.subheader('For the following questions, move the slider to indicate your agreement with the statement.')
    st.markdown("")
    st.markdown("")
    st.info('Please indicate from -1 = Strongly disagree to 100 = Strongly agree')

    st.markdown("")
    st.markdown("")
    var36O237 = st.slider(
        '"I am willing to invest time and energy to get the most out of the game."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var36O238 = st.slider(
        '"I enjoy spending time carefully selecting formations and tactics."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var36O240 = st.slider(
        '"I want to quickly progress to the next levels."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var36O241 = st.slider(
        '"I prefer challenging gameplay that requires skills."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var36O242 = st.slider(
        '"I enjoy competition as it allows me to measure my own success."',
        -1.0, 100.0, 50.0, 1.0)


    st.markdown("")
    st.markdown("")
    var36O248 = st.slider(
        '"I like to play football video games as a way of connecting with my friends and family."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var36O249 = st.slider(
        '"I enjoy giving in-game gifts to my friends and family."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var36O252 = st.slider(
        '"I enjoy adding upgrades to my football club (eg. gyms, training facilities, etc.)"',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var36O253 = st.slider(
        '"I enjoy gambling and/or placing bets on game outcomes."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O274 = st.slider(
        '"I am able to get consistently better at this game."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O275 = st.slider(
        '"I have many ways to upgrade the skills of my squad so they perform better on the pitch."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O276 = st.slider(
        '"There are many ways to earn prizes / achievements / in-game currency within this game."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O277 = st.slider(
        '"I feel challenged by this game when I play it."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O279 = st.slider(
        '"I like the set-up of the leaderboard mechanics of this game."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O280 = st.slider(
        '"The game provides concrete objectives for progressing in the game."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O281 = st.slider(
        '"I feel in control of the overall gameplay."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O282 = st.slider(
        '"I value the achievements within this game."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var41O283 = st.slider(
        '"I want to be admired for the achievements I receive in this game."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var42O285 = st.slider(
        '"The layout of information in the game is very clear and not overwhelming."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var42O286 = st.slider(
        '"The ability to select team formations on the pitch is clear and precise."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var42O287 = st.slider(
        '"There are many ways to influence my squad member’s personality, behaviour, and training to lead my team to victory (eg. cooperation with team-mates, professionalism, fitness)."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var42O289 = st.slider(
        '"There are many ways to improve the popularity of my club so that they’re able to perform better as a team over multiple games."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var42O290 = st.slider(
        '"I find this game very entertaining."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    var44O298 = st.slider(
        '"I would rather see ads than pay for games."',
        -1.0, 100.0, 50.0, 1.0)

    st.markdown("")
    st.markdown("")
    st.markdown("")
    var46O315 = st.slider(
        '"I play football video games to engage with popular video game streamers (eg. on Twitch, YouTube, etc.)."',
        -1.0, 100.0, 50.0, 1.0)

    output = ""

    input_dict = {'var2': var2,
                  'var4O13': var4O13,
                  'var31': var31,
                  'var32': var32,
                  'var35': var35,
                  'var36O237': var36O237,
                  'var36O242': var36O242,
                  'var36O238': var36O238,
                  'var36O240': var36O240,
                  'var36O241': var36O241,
                  'var36O248': var36O248,
                  'var36O249': var36O249,
                  'var36O252': var36O252,
                  'var36O253': var36O253,
                  'var37O256': var37O256,
                  'var41O274': var41O274,
                  'var41O275': var41O275,
                  'var41O276': var41O276,
                  'var41O277': var41O277,
                  'var41O279': var41O279,
                  'var41O280': var41O280,
                  'var41O281': var41O281,
                  'var41O282': var41O282,
                  'var41O283': var41O283,
                  'var42O285': var42O285,
                  'var42O286': var42O286,
                  'var42O287': var42O287,
                  'var42O289': var42O289,
                  'var42O290': var42O290,
                  'var44O298': var44O298,
                  'var46O315': var46O315,}
    input_df = pd.DataFrame([input_dict])

    if st.button("Predict"):
        output = predict(model=model, input_df=input_df)
        output = str(output)

    st.header('Recommendation likelihood: {}'.format(output))

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.caption(
        'Disclaimer: This app is for simulation purposes only and does not reflect unknown market forces. Extreme slider combinations may produce extreme results.')


if __name__ == '__main__':
    run()

