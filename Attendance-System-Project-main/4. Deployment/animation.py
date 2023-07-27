import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_m9ub4f.json"
#lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(lottie_url_hello)
#lottie_download = load_lottieurl(lottie_url_download)


# st_lottie(lottie_hello, key="hello")

# if st.button("Download"):
#     with st_lottie_spinner(lottie_download, key="download"):
#         time.sleep(5)
#     st.balloons()
    

col1,col2=st.columns([0.2,3])
def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_m9ub4f.json"

with col1:
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, key="hello",width=30)
    #st_lottie(lottie_hello, key="hello",width=50)
with col2:
    st.write('1:---------')
    #st.write(st_lottie(lottie_hello, key="hell",width=50),'1:---------')
    st.write('2:-----------')
    





# #-----------------------------------
# import base64
# file_ = open("F:/CCS Attendance system/17882-face-recognition.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

# # st.markdown(
# #     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
# #     unsafe_allow_html=True,
# # )

# st.image("F:/CCS Attendance system/17882-face-recognition.gif",format='GIF')





  