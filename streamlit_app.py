import glob

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
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        st.write("Width: " + str(width))
        st.write("Height: " + str(height))
        st.write("FPS: " + str(fps))
        st.write("Total Frames: " + str(total_frames))

    # success, image = cap.read()
    # count = 0

    # while success:
    #  success, image = cap.read()
    #  count += 1


if __name__ == "__main__":
    main()
