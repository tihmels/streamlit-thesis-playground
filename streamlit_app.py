import streamlit as st
import time
import glob

VIDEO_DIR = "videos"
videos = glob.glob(VIDEO_DIR + "/*.mp4")

t = st.empty()


def load_video(video):
    st.write("called")
    video_file = open(video, 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)


option = st.sidebar.selectbox(
    "Select a video", videos, format_func=lambda l: l.split("/", 1)[1], on_change=load_video)

st.write('You selected:', option)

st.title("Thesis Playground")
