import streamlit as st
import time
import glob

VIDEO_DIR = "videos"
videos = glob.glob(VIDEO_DIR + "/*.mp4")

add_selectbox = st.sidebar.selectbox(
    "Select video to inspect", videos
)

st.title("TEST")
