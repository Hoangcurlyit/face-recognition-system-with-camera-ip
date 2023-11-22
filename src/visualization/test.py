import cv2
from ultralytics import YOLO
import os
from skip_frame import skip_frames, display_frame, close_video_stream, open_video_stream
# Khởi tạo mô hình YOLO
model = YOLO('C:/Users/20521/OneDrive/Desktop/CV/face-recognition-system-with-camera-ip/models/yolov8n-face.pt') 

def open_video_stream(source_url):
    cap = cv2.VideoCapture(source_url)
    if not cap.isOpened():
        print("Không thể mở video stream.")
        return None
    return cap

def close_video_stream(cap):
    if cap is not None:
        cap.release()

def save_cropped_face(frame, box, save_dir, idx):
    # Chuyển đổi định dạng bbox sang xyxy
    xyxy_box = box.xyxy.int().tolist()

    # Xử lý từng bounding box một cách riêng lẻ
    for single_box in xyxy_box:
        # Đảm bảo rằng single_box có đúng số giá trị mong đợi
        if len(single_box) == 4:
            # Cắt và lưu hình ảnh từ frame gốc
            x, y, x2, y2 = single_box
            cropped_face = frame[y:y2, x:x2]
            save_path = os.path.join(save_dir, f"face_{idx}_{x}_{y}_{x2}_{y2}.jpg")
            cv2.imwrite(save_path, cropped_face)
            print(f"Đã lưu hình ảnh khuôn mặt tại {save_path}")
        else:
            print(f"Định dạng bbox không hợp lệ: {single_box}")

def process_video(source_url, num_skip_frames, save_dir):
    cap = open_video_stream(source_url)
    if cap is not None:
        # Tạo thư mục lưu trữ nếu nó chưa tồn tại
        os.makedirs(save_dir, exist_ok=True)

        while True:
            skip_frames(cap, num_skip_frames)
            
            # Đọc frame từ video
            ret, frame = cap.read()
            if not ret:
                break
            
            # Áp dụng YOLO để phát hiện khuôn mặt
            results = model(frame, show=True)

            # Lưu hình ảnh khuôn mặt vào thư mục đã chỉ định
            for idx, result in enumerate(results):
                boxes = result.boxes
                for box in boxes:
                    save_cropped_face(frame, box, save_dir, idx)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        close_video_stream(cap)

if __name__ == "__main__":
    source_url = "rtsp://admin:clbAI_2023@192.168.1.69"
    num_skip_frames = 10
    save_directory = 'C:/Users/20521/OneDrive/Desktop/CV/face-recognition-system-with-camera-ip/src/data/face'
    process_video(source_url, num_skip_frames, save_directory)
