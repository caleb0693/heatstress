

import pandas as pd
import numpy as np
import altair as alt
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import streamlit as st
st.title('Heat Stress ML Application')
st.write('##### Created by: Caleb Ginorio MS, CSP')
st.write(
    " ###### This app calculates the probablity of having an intervetion based on a number of inputs"
)

col1, col2, col3 = st.columns(3)

img_file2 = "worker2.png"
st.image(img_file2, width =700)


age = st.number_input('Worker Age',
                min_value= 1,
                max_value= 99,
                value=25)


respirator = st.radio("Respirator required?",
            options= ["Yes",
                      "No",
                        ])



ppe = st.multiselect("Select PPE Required", 
             options = ["None",
                        "One Pair of Coveralls",
                        "Two Pair of Coveralls",
                        "Plastic Suit",
                        "Chemical Suit",
                        ])


activity_level = st.radio("Activity Level", 
             options = ["Light",
                        "Moderate",
                        "Intense",
                        ])


work_area = st.multiselect("Work Area Conditions (Select all that apply)", 
                 options = ["Indoor",
                        "Outdoor",
                        "Direct Sunlight",
                        "Shade"
                         ])


months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

month = st.selectbox("Select a Month", months)


time = st.selectbox("Time",     
                 options = ["0600-1200",
                        "1200-1800",
                        "1800-2400",
                        "0000-0600"
                         ])

temperature = st.slider("Temperature (F)", 60,150)

rh = st.slider("Relative Humidity (%)", 0,100)

monitor = st.selectbox("Monitor Experiencel Level", 
                 options = ["Entry Level",
                        "Mid-Career",
                        "Senior"
                         ])






