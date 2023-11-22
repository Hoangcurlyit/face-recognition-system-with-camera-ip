import cv2

def open_video_stream(source_url):
    cap = cv2.VideoCapture(source_url)
    if not cap.isOpened():
        print("Error opening video stream or file")
        return None
    return cap

def close_video_stream(cap):
    cap.release()
    cv2.destroyAllWindows()

def skip_frames(cap, num_frames):
    for _ in range(num_frames):
        cap.grab()
def display_frame(cap):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        return True
    return False

def process_video(source_url, num_skip_frames):
    cap = open_video_stream(source_url)

    if cap is not None:
        while True:
            skip_frames(cap, num_skip_frames)

            if not display_frame(cap):
                break

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        close_video_stream(cap)

if __name__ == "__main__":
    source_url = "rtsp://admin:clbAI_2023@192.168.1.69"
    num_skip_frames=15
    process_video(source_url,num_skip_frames)