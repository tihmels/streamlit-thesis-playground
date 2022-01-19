import glob

import streamlit as st

VIDEO_DIR = "videos"
videos = glob.glob(VIDEO_DIR + "/*.mp4")

st.title("Thesis Playground")


def load_video(video):
    video_file = open(video, 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)


option = st.sidebar.selectbox("Select a video", videos, format_func=lambda l: l.split("/", 1)[1])

load_video(option)