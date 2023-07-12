import requests
import streamlit as st
import pickle
import sklearn
# from Downloads import acm_feature_extraction
from feature_extraction import feature_extractor
pickle_in = open("Phishing_Detector_Model_DT_7.pkl", "rb")
clf = pickle.load(pickle_in)

import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-whois'])
classes = ['Legitimate', 'Phishing']

from streamlit_lottie import st_lottie #-- we will need request and this to access json data of that animation
st.set_page_config(page_title="URL Detection", layout= 'wide')
st.title('Group: 5 - Machine Learning 	:computer:')
st.subheader('~ Arijeet Mukhopadhyay & Akanksha Rathod')


#-- to json data of that animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


#--- Animation ---
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_uqiitjs4.json")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title(':fishing_pole_and_fish:  PhishWatch')
        url =st.text_input('Enter your URL: ')
        pred = st.button("Search")
        if pred:
            input = feature_extractor(url)
            y_pred = clf.predict(input)
            st.write(classes[y_pred.item()])





    with right_column:
        st_lottie(lottie_coding, height = 250, key = "phishing")


#-------- PICKLE --------



