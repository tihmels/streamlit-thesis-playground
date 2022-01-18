import streamlit as st
import time
import glob

VIDEO_DIR = "videos"
videos = glob.glob(VIDEO_DIR + "/*.mp4")

t = st.empty()

def load_main_page(video):
    video_file = open(video, 'rb')
    video_bytes = video_file.read()

    t.video(video_bytes)

add_selectbox = st.sidebar.selectbox(
    "Select a video", videos, format_func = lambda l:l.split("/", 1)[1], on_change=load_main_page
)

st.title("TEST")
