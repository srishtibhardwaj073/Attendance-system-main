
import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_option_menu import option_menu
import cv2
import numpy as np
import os
import glob
import os.path
import pickle
import streamlit_authenticator as stauth
from pathlib import Path
import webbrowser
import time
from streamlit_lottie import st_lottie
import requests


st.set_page_config(
    page_title="Attendance System", page_icon="📊", layout="wide"
)
st.image("D:\\p1 html\\Attendance-System-Project-main\\4. Deployment\\logo.jpg")
hide_st_style="""
              <style>
              #MainMenu {visibility: hidden;}
              footer {visibility: hidden;}
              </style>
              """
st.markdown(hide_st_style, unsafe_allow_html=True)


selected2 = option_menu(None, ["Home", "Add_New_Student","Attendance_with_camera","Manual_Attendance"], 
    icons=['house', 'person-bounding-box','person-bounding-box','person-bounding-box'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)
if selected2 == "Home":
    st.title("Steps to register your face.")
    
    

    col1,col2=st.columns([0.15,3])
    def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
    lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_m9ub4f.json"

    with col1:
        lottie_hello = load_lottieurl(lottie_url_hello)
        st_lottie(lottie_hello, key="1",width=30)
        st_lottie(lottie_hello, key="2",width=30)
        st_lottie(lottie_hello, key="3",width=30)
        st_lottie(lottie_hello, key="4",width=30)
        st_lottie(lottie_hello, key="5",width=30)
        st_lottie(lottie_hello, key="6",width=30)
        st_lottie(lottie_hello, key="7",width=30)


    with col2:
        st.write('Hi I am AI')
        st.write(' ')
        st.write('Hi I am AI')
        st.write(' ')
        st.write('Hi I am AI')
        st.write(' ')
        st.write('Hi I am AI')
        st.write(' ')
        st.write('Hi I am AI')
        st.write(' ')
        st.write('Hi I am AI')
        st.write(' ')
        st.write('Hi I am AI')





#---------------------------------------------------------


#------------Face Login page open 3 camera------------------
if selected2 == "Face Register":
    #st.header("Face Login")
    st.subheader("Follow the steps on the home page to register your face.")
    # image_name = st.text_input('Enter your Name:')
    name = st.text_input('Enter your Name:')
    email = st.text_input('Enter your Email:')
    path0 ='F:\CCS Attendance system\datasets' 
    path=os.path.join(path0,name)
    if st.checkbox('I agree'):
        if os.path.exists(path):
            st.warning('User Name already exits', icon="⚠️")
        
        else: os.mkdir(path)

    
    #my_bar = st.progress(10)

    # for percent_complete in range(10):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)

    tab1, tab2, tab3 = st.tabs(["Font Profile", "Left Profile", "Right Profile"])
    with tab1:
        #st.header("Click your Font Profile")
        st.info("Follow the instructions on right side !")
        left,right = st.columns([1,1])
        


        with left:
            img_file_buffer = st.camera_input("Click your Font Profile")
            
            # path0 ='F:\CCS Attendance system'
            image_name='front.jpg'
            # path=os.path.join(path0,name)

            # if os.path.exists(path):
            #     st.warning('fail')
            # else: os.mkdir(path)
            

            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                bytes_data = img_file_buffer.getvalue()
                cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
                
                
                os.chdir(path)
                cv2.imwrite(image_name,cv2_img)
                 
            else: 
                st.button('Save Front Profile')
                # cv2.imwrite(image_name,cv2_img)


        # with centre:
        #     def load_lottieurl(url: str):
        #         r = requests.get(url)
        #         if r.status_code != 200:
        #             return None
        #         return r.json()
        #     lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_m9ub4f.json"
        #     lottie_hello = load_lottieurl(lottie_url_hello)
        #     st.write('  ')
        #     st.write('  ')
        #     st.write('  ')
        #     st.write('  ')
        #     st.write('  ')
        #     st_lottie(lottie_hello, key="hello",width=25)
        #     st_lottie(lottie_hello, key="hell",width=25)
            
                




        with right:
            st.subheader("Instructions !")
            st.write("hello i an ai--------")
            st.write('hello i am ai--------')
            st.write('3---------')
            


    with tab2:
        st.info("Follow the instructions on right side !")
        left,right = st.columns([1,1])
        with left:
            img_file_buffer = st.camera_input("Click your Left Profile")
            image_name='hi.jpg'
            path ='F:\CCS Attendance system'
            image_name='left.jpg'

            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                bytes_data = img_file_buffer.getvalue()
                cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
                path=os.path.join(path0,name)
                os.chdir(path)
                cv2.imwrite(image_name,cv2_img) 
            if st.button('Save Left Profile'):
                cv2.imwrite(image_name,cv2_img)

        with right:
            st.subheader("Instructions !")
            st.write("1:--------")
            st.write('2:--------')
            st.write('3---------')
       

    with tab3:
        st.info("Follow the instructions on right side !")
        left,right = st.columns([1,1])
        with left:
            img_file_buffer = st.camera_input("Click your Right Profile")
            image_name='hi.jpg'
            path ='F:\CCS Attendance system'
            image_name='right.jpg'

            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                bytes_data = img_file_buffer.getvalue()
                cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
                path=os.path.join(path0,name)
                os.chdir(path)
                cv2.imwrite(image_name,cv2_img) 
            if st.button('Save Right Profile'):
                cv2.imwrite(image_name,cv2_img)

        with right:
            st.subheader("Instructions !")
            st.write("1:--------")
            st.write('2:--------')
            st.write('3---------')

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'adarsh'
# app.run(port=1234)

hide_menu_style = """
        <style>
        MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

