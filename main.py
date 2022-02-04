import glob
import os

import cv2
import numpy as np
import streamlit as st

from VideoData import VideoData

st.set_page_config(
    page_title="Thesis Playground App",
    layout="wide",
    initial_sidebar_state="expanded"
)

VIDEO_DIR = "videos"
FRAMES_TMP = "tmp"


def main():
    videos = glob.glob(os.path.join(VIDEO_DIR, "*.mp4"))
    selected_option = st.sidebar.selectbox("Select video for inspection", videos,
                                           format_func=lambda l: l.split("/", 1)[1])

    load_video(selected_option)


def load_video(video):
    st.title(video.split("/", 1)[1])

    video_stream = open(video, 'rb')
    video_bytes = video_stream.read()

    st.video(video_bytes)

    cap = cv2.VideoCapture(video)

    vd = extract_video_data(cap)

    set_sidebar_info(vd)

    # frames = extract_frames_from_video(cap)

    # st.write(frames.shape)

    # video_range = st.slider(
    #    "Select video range:",
    #    value=(time(0, 0), time(0, vd.minutes, vd.seconds)),
    #    min_value=(time(0, 0, 0)),
    #    max_value=(time(0, vd.minutes, vd.seconds)),
    #    step=timedelta(0, 1),
    #    format="mm:ss"
    # )

    # success, image = cap.read()
    # count = 0

    # while success:
    #  success, image = cap.read()
    #  count += 1


def extract_video_data(cap: cv2.VideoCapture):
    if cap.isOpened():
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        return VideoData(frame_width, frame_height, frame_count, fps)


def extract_frames_from_video(cap):
    frames = []

    ret = True
    while ret:
        ret, frame = cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # frames.append(frame)

    return np.stack(frames, axis=0)


def set_sidebar_info(video_data: VideoData):
    col1, col2 = st.sidebar.columns(2)

    with col1:
        st.text("Dimensions")
        st.text("Total Frames")
        st.text("FPS")
        st.text("Duration (s)")
        st.text("Duration (m:s)")

    with col2:
        st.markdown("<p style='text-align: right;'>" + str(video_data.frame_width) + " x " + str(
            video_data.frame_height) + "</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: right;'>" + str(video_data.frame_count) + "</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: right;'>" + str(video_data.fps) + "</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: right;'>" + str(video_data.duration) + "</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: right;'>" + str(video_data.minutes) + ":" + str(video_data.seconds) + "</p>",
                    unsafe_allow_html=True)


if __name__ == "__main__":
    main()
