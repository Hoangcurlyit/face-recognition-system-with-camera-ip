import cv2
from skip_frame import capture_rtsp_video_frames_generator, display_frames

if __name__ == "__main__":
    source_url = "rtsp://admin:clbAI_2023@192.168.1.69"
    skip_frames = 10
    frames_generator = capture_rtsp_video_frames_generator(source_url, skip_frames)
    # Call the function to display frames
    display_frames(source_url, skip_frames)