from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# RTSP 스트림 URL들
rtsp_url1 = 'rtsp://'
rtsp_url2 = 'rtsp://'
rtsp_url3 = 'rtsp://'

# VideoCapture 객체 생성
cap1 = cv2.VideoCapture(rtsp_url1, cv2.CAP_FFMPEG)
cap2 = cv2.VideoCapture(rtsp_url2, cv2.CAP_FFMPEG)
cap3 = cv2.VideoCapture(rtsp_url3, cv2.CAP_FFMPEG)

# frame size
f_width = 500
f_height = 400

# 이미지 품질과 파일 크기 간의 균형 ( 0 ~ 100 )
compression_level = 50

# MJPEG 스트리밍 함수
def generate_frames(cap):
    while True:
        success, frame = cap.read()
        
        # cap.grab()  # 버퍼에서 다음 프레임을 가져옴
        # success, frame = cap.retrieve()  # 실제 프레임을 얻어옴
        if not success:
            print("Failed to read frame")
            break

        frame = cv2.resize(frame, (f_width, f_height))
        # 압축 품질 조절
        ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, compression_level])
        if not ret:
            print("Failed to encode frame")
            break

        print("Frame size after encoding:", len(buffer.tobytes()))

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# 라우트 및 템플릿
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed1')
def video_feed1():
    return Response(generate_frames(cap1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(generate_frames(cap2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed3():
    return Response(generate_frames(cap3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8092, debug=True)
