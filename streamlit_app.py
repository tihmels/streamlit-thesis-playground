import glob
from datetime import time
from datetime import timedelta

import cv2
import streamlit as st

VIDEO_DIR = "videos"
videos = glob.glob(VIDEO_DIR + "/*.mp4")


def main():
    selected_option = st.sidebar.selectbox("Select video", videos, format_func=lambda l: l.split("/", 1)[1])
    load_video(selected_option)


def load_video(video):
    st.title(video.split("/", 1)[1])

    video_file = open(video, 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    cap = cv2.VideoCapture(video)

    if cap.isOpened():
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = frame_count / fps

        st.write("Width: " + str(frame_width))
        st.write("Height: " + str(frame_height))
        st.write("FPS: " + str(fps))
        st.write("Frame count: " + str(frame_count))
        st.write('Duration (S) = ' + str(duration))
        minutes = int(duration / 60)
        seconds = int(duration % 60)
        st.write('Duration (M:S) = ' + str(minutes) + ':' + str(seconds))

    appointment = st.slider(
        "Schedule your appointment:",
        min_value=(time(0, 0, 0)),
        max_value=(time(0, minutes, seconds)), step=timedelta(0, 1))

    # success, image = cap.read()
    # count = 0

    # while success:
    #  success, image = cap.read()
    #  count += 1


if __name__ == "__main__":
    main()
