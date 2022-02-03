import glob
from datetime import time
from datetime import timedelta

import cv2
import streamlit as st

st.set_page_config(
    page_title="Thesis Playground App",
    layout="wide",
    initial_sidebar_state="expanded"
)

VIDEO_DIR = "videos"


def main():
    videos = glob.glob(VIDEO_DIR + "/*.mp4")
    selected_option = st.sidebar.selectbox("Select video for inspection", videos,
                                           format_func=lambda l: l.split("/", 1)[1])

    print("TEST")
    load_video(selected_option)


def load_video(video):
    st.title(video.split("/", 1)[1])

    video_stream = open(video, 'rb')
    video_bytes = video_stream.read()

    st.video(video_bytes)

    cap = cv2.VideoCapture(video)

    if cap.isOpened():
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        duration = frame_count / fps
        minutes = int(duration / 60)
        seconds = int(duration % 60)

        video_range = st.slider(
            "Select video range:",
            value=(time(0, 0), time(0, minutes, seconds)),
            min_value=(time(0, 0, 0)),
            max_value=(time(0, minutes, seconds)),
            step=timedelta(0, 1),
            format="mm:ss"
        )

        col1, col2 = st.sidebar.columns(2)

        with col1:
            st.text("Dimensions")
            st.text("Total Frames")
            st.text("FPS")
            st.text("Duration (s)")
            st.text("Duration (m:s)")

        with col2:
            st.markdown("<p style='text-align: right;'>" + str(frame_width) + " x " + str(frame_height) + "</p>",
                        unsafe_allow_html=True)
            st.markdown("<p style='text-align: right;'>" + str(frame_count) + "</p>",
                        unsafe_allow_html=True)
            st.markdown("<p style='text-align: right;'>" + str(fps) + "</p>",
                        unsafe_allow_html=True)
            st.markdown("<p style='text-align: right;'>" + str(duration) + "</p>",
                        unsafe_allow_html=True)
            st.markdown("<p style='text-align: right;'>" + str(minutes) + ":" + str(seconds) + "</p>",
                        unsafe_allow_html=True)

        # success, image = cap.read()
        # count = 0

        # while success:
        #  success, image = cap.read()
        #  count += 1


if __name__ == "__main__":
    main()
