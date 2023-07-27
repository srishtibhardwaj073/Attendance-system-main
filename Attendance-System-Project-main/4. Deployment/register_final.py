import streamlit as st
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
from Preparing_local import prepare_test_img, test
import face_recognition


st.set_page_config(page_title='CCS Attendance System',page_icon="logo.ico",layout="centered")

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Green Illustrative Accounting Service Website.png')
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://www.ccscomputers.co.in/" target="_blank">CCS COMPUTERS PVT LTD</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



# with st.sidebar:
#     selected = option_menu(
#         menu_title= None,
#         options=["Home", "Face Login", "Id Login"],
#         menu_icon="cast", default_index=0, orientation="horizontal"
#     )

# selected2 = option_menu(None, ["Home", "Face Register"], 
#     icons=['house', 'Person bounding box'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

selected2 = option_menu(None, ["Home", "Face Register","Face Login"], 
    icons=['house', 'person-bounding-box'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)
#------------button color-------------------------------
m = st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: #0099ff;
                color:#ffffff;
            }
            div.stButton > button:hover {
                background-color: #00ff00;
                color:#ff0000;
                }
            </style>""", unsafe_allow_html=True)
#----------------------------------------------

#-----------------------------------

#----------------------------------------
        






#----------------Home Page----------------------
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
    path0 ='F:\CCS Attendance system\db' 
    # path=os.path.join(path0,name)
    # if st.checkbox('I agree'):
    #     if os.path.exists(path):
    #         st.warning('User Name already exits', icon="⚠️")
        
    #     else: os.mkdir(path)
    
    #my_bar = st.progress(10)

    # for percent_complete in range(10):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)

    tab1, tab2= st.tabs(["Upload Profile","Instructions !"])
    with tab1:
        #st.header("Click your Font Profile")
        st.info("Follow the instructions in next Tab !")
        left,right = st.columns([1,1])
        


        with left:
            img_file_buffer = st.camera_input("Upload your Profile")
            
            # path0 ='F:\CCS Attendance system'
            image_name=name+'.jpg'
            # path=os.path.join(path0,name)

            # if os.path.exists(path):
            #     st.warning('fail')
            # else: os.mkdir(path)
            

            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                bytes_data = img_file_buffer.getvalue()
                cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
                
                
                os.chdir(path0)
                cv2.imwrite(image_name,cv2_img)
                 
            else: 
                st.button('Save Front Profile')

                if st.button('Complete Registration'):
                    path = "F:\CCS Attendance system\db"

                    def training(path):
                        images = os.listdir(path)  
                        encoded_trains =[]

                        for image in images:
                            train_img = face_recognition.load_image_file(f"F:\CCS Attendance system\db/{image}")
                            train_img = cv2.cvtColor(train_img,cv2.COLOR_BGR2RGB)
                            encoded_trains.append(face_recognition.face_encodings(train_img)[0])
                        return encoded_trains, images


                    encoded_trains, images = training(path)
                    # st.write(images)
                    output_file = 'encoded_faces.pickle'
                    with open(output_file, 'wb') as f_out:
                        pickle.dump(encoded_trains, f_out)
                    st.success('Registration Done')

                    
                


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
            st.write(' ')
            # st.subheader("Instructions !")
            # st.write("hello i an ai--------")
            # st.write('hello i am ai--------')
            # st.write('3---------')
            


    # with tab2:
    #     st.info("Follow the instructions on right side !")
    #     left,right = st.columns([1,1])
    #     with left:
    #         img_file_buffer = st.camera_input("Click your Left Profile")
    #         image_name='hi.jpg'
    #         path ='F:\CCS Attendance system'
    #         image_name='left.jpg'

    #         if img_file_buffer is not None:
    #             # To read image file buffer with OpenCV:
    #             bytes_data = img_file_buffer.getvalue()
    #             cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    #             path=os.path.join(path0,name)
    #             os.chdir(path)
    #             cv2.imwrite(image_name,cv2_img) 
    #         if st.button('Save Left Profile'):
    #             cv2.imwrite(image_name,cv2_img)

    #     with right:
    #         st.subheader("Instructions !")
    #         st.write("1:--------")
    #         st.write('2:--------')
    #         st.write('3---------')
       

    # with tab3:
    #     st.info("Follow the instructions on right side !")
    #     left,right = st.columns([1,1])
    #     with left:
    #         img_file_buffer = st.camera_input("Click your Right Profile")
    #         image_name='hi.jpg'
    #         path ='F:\CCS Attendance system'
    #         image_name='right.jpg'

    #         if img_file_buffer is not None:
    #             # To read image file buffer with OpenCV:
    #             bytes_data = img_file_buffer.getvalue()
    #             cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    #             path=os.path.join(path0,name)
    #             os.chdir(path)
    #             cv2.imwrite(image_name,cv2_img) 
    #         if st.button('Save Right Profile'):
    #             cv2.imwrite(image_name,cv2_img)

    #     with right:
    #         st.subheader("Instructions !")
    #         st.write("1:--------")
    #         st.write('2:--------')
    #         st.write('3---------')

if selected2 == "Face Login":
    st.title("Check Login via Face.")
    from Preparing_local import prepare_test_img, test
    def load_model():
        with open ('F:\Attendance_System-main\encoded_faces.pickle', 'rb') as f_in:
            encoded_trains = pickle.load(f_in)
        return encoded_trains
    encoded_trains = load_model()



    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        _, test_img = camera.read()
        test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
        test_img_small = cv2.resize(test_img,(0,0),None,0.5,0.5)

        face_test_locations = face_recognition.face_locations(test_img_small, model = "hog")
        encoded_tests = face_recognition.face_encodings(test_img_small)
        df = test(encoded_tests, face_test_locations, test_img, encoded_trains)#,attendance_file)
                
        #st.success("Success")
        #st.image(test_img)
        FRAME_WINDOW.image(test_img)
        #st.write(df)
    else:
        st.write('Stopped')


    



































hide_menu_style = """
        <style>
        MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


