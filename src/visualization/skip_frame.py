import cv2
def capture_rtsp_video_frames_generator(source_url, skip_frames=10):
    # Create a VideoCapture object and read from the specified URL
    cap = cv2.VideoCapture(source_url)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    try:
        # Read until video is completed
        while True:
            # Skip frames if necessary
            for _ in range(skip_frames):
                cap.grab()

            # Read the next frame
            ret, frame = cap.read()

            if ret:
                # Yield the frame for processing
                yield frame
            else:
                break

    finally:
        # Release the video capture object
        cap.release()
def display_frames(source_url, skip_frames=10):
    # Create a generator object
    frames_generator = capture_rtsp_video_frames_generator(source_url, skip_frames)

    # Display frames one by one
    for frame in frames_generator:
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture object
    cv2.destroyAllWindows()
# Example usage:
if __name__ == "__main__":
    source_url = "rtsp://admin:clbAI_2023@192.168.1.69"
    skip_frames = 10

    # Create a generator object
    frames_generator = capture_rtsp_video_frames_generator(source_url, skip_frames)

    # Process frames one by one
    for frame in frames_generator:
        # Perform your processing on each frame here
        pass
