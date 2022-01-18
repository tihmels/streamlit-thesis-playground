import streamlit as st
import time
import glob

VIDEO_DIR = "videos"
videos = glob.glob(VIDEO_DIR + "/*.mp4")

add_selectbox = st.sidebar.selectbox(
    "Select a video", videos, format_func = lambda l:l.split("/", 1)[1]
)

st.title("TEST")
