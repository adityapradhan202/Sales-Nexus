import streamlit as st
from predicting_func import predict_nsales
import time
from predicting_model import percentage_accuracy_mae as pam

# session state
if 'avg_w_exp' not in st.session_state:
    st.session_state.avg_w_exp = 0
if 'tv_ad_exp' not in st.session_state:
    st.session_state.tv_ad_exp = 0
if 'n_radio_ad' not in st.session_state:
    st.session_state.n_radio_ad = 0
if 'online_ad_exp' not in st.session_state:
    st.session_state.online_ad_exp = 0

def set_stsvars_none():
    st.session_state.avg_w_exp = 0
    st.session_state.tv_ad_exp = 0
    st.session_state.n_radio_ad = 0
    st.session_state.online_ad_exp = 0

st.header('Sales nexus')
tab_names = ['Main page', 'About']
tab1, tab2 = st.tabs(tabs=tab_names)

with tab1:
    
    st.markdown('##### Enter all the respective values, and let the machine learning model predict the sales for you :smile:')

    x1 = st.number_input(label='Average weekly expenses (On a scale of 0-60 Grands)', min_value=0, max_value=60, key='avg_w_exp')
    x2 = st.number_input(label='Television ads expenses (On a scale of 0-200 dollars)', min_value=0, max_value=200, key='tv_ad_exp')
    x3 = st.number_input(label='Number of radio ads (On a scale of 0-3000 dollars)', min_value=0, max_value=3000, key='n_radio_ad')
    x3 = int(x3)
    x4 = st.number_input(label='Online ads expenses (On a scale of 0-3000 dollars)', min_value=0, max_value=3000, key='online_ad_exp')

    features = [x1, x2, x3, x4]

    psales_btn = st.button(label='Predict Sales', type='primary')
    if psales_btn:
        with st.spinner(text='Wait for a few seconds...'):
            time.sleep(3)
            st.write(f'Predicted sales: :orange[{round(predict_nsales(features))}] products might be sold this week! :smile:')

            refresh_btn = st.button(label='Click here to predict again!', type='primary', on_click=set_stsvars_none)
            if refresh_btn:
                st.rerun()

with tab2:
    st.subheader('About this app...')
    st.write("""Introducing Sales Nexus, a cutting-edge app revolutionizing sales forecasting. With Sales Nexus, simply input your weekly advertising expenses, TV ad spend, average weekly expenses, and radio ads frequency, and let our advanced linear regression algorithm do the rest. By harnessing the power of machine learning, Sales Nexus predicts the number of products you can expect to sell in a week with remarkable accuracy. Say goodbye to guesswork and hello to data-driven decision-making with Sales Nexus.""")

    st.write(f':orange[Disclaimer:] The error percentage of this app is :orange[{round(pam)}] percent! So, it is accurate to a considerable extent, but it is not that accurate!')
    st.write(f'This app is just a prototype designed, built, and made for University group activity/group project only :sweat_smile:')
