import streamlit as st
import glob
import cv2


VIDEO_DIR = "videos"
videos = glob.glob(VIDEO_DIR + "/*.mp4")

st.title("Thesis Playground")


def main():
    selected_option = st.sidebar.selectbox("Select video", videos, format_func=lambda l: l.split("/", 1)[1])
    load_video(selected_option)


def load_video(video):
    st.subheader(video.split("/", 1)[1])

    video_file = open(video, 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    cap = cv2.VideoCapture(video)

    if cap.isOpened():
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        st.write("Width: " + width)
        st.write("Height: " + height)
        st.write("FPS: " + fps)
        st.write("Total Frames: " + total_frames)

    # success, image = cap.read()
    # count = 0

    # while success:
    #  success, image = cap.read()
    #  count += 1


if __name__ == "__main__":
    main()
