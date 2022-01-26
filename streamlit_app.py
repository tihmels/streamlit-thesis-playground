import glob
from datetime import time
from datetime import timedelta

import cv2
import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

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
        "Select video range:",
        value=(time(0, 0), time(0, minutes, seconds)),
        min_value=(time(0, 0, 0)),
        max_value=(time(0, minutes, seconds)),
        step=timedelta(0, 1),
        format="mm:ss"
    )



    # success, image = cap.read()
    # count = 0

    # while success:
    #  success, image = cap.read()
    #  count += 1


if __name__ == "__main__":
    main()
