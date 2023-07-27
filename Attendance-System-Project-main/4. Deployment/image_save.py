import streamlit as st
import cv2
import numpy as np
import os
import glob
import os.path
path = "F:\CCS Attendance system\image"
image_name="xyz.jpg"
img_file_buffer = st.camera_input(" ")

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    os.chdir(path)
    cv2.imwrite(image_name,cv2_img) 
    st.write('h')
if st.button('Save Image'): cv2.imwrite(image_name,cv2_img) 
st.write('h')


