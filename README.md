https://wooono.tistory.com/701
가상환경 사용법 - 일반적으로 프로젝트 간 패키지 충돌을 방지하기 위해 사용

python study
https://wikidocs.net/81078

# 가상환경 생성
python3 -m venv rtsp

# 활성화
source .venv/bin/activate

# 패키지 설치
pip install 패키지이름

# 패키지 목록
pip list

# 비활성화
deactivate

# pip upgrade 23.1.2 > 23.2.1
pip install --upgrade pip

# opencv
pip install opencv-python

# cv2.VideoCapture를 통한 rtsp 스트리밍 테스트
계속적으로 카메라에 있는 프레임을 찍어낸다. 끊기는 현상 발생

# rtsp_connection.py
여러 rtsp cctv영상 송출

# rtsp_func.py
함수로 빼서 각각 실행했지만 첫번째 영상이 꺼져야 그다음 영상이 보여짐

# rtsp_thread.py
각 창에 대한 별도의 스레드를 사용하여 처리할 수 있습니다. 멀티스레드를 사용하여 여러 RTSP 스트림을 동시에 표시
멀티스레딩 실행 실패 - 멀티스레딩에 대한 지원이 제한

# rtsp_processing.py
OpenCV와 멀티스레딩의 호환성 문제를 피하기 위해 멀티프로세싱을 사용
> cv2.VideoCapture(rtsp_url)로 RTSP 스트림을 캡처하기 위한 VideoCapture 객체를 생성합니다.
> cv2.imshow(window_name, frame)으로 프레임을 지정된 창에 표시합니다.
> cap.release()로 VideoCapture 객체를 해제합니다.
> cv2.destroyAllWindows()로 OpenCV 창을 모두 닫습니다.
> Process를 사용하여 각 RTSP 스트림을 처리하는 별도의 프로세스를 시작합니다.
> process.start()로 프로세스를 시작하고, process.join()으로 프로세스가 종료될 때까지 대기합니다.

# 스레드와 프로세스
스레드: 프로세스 내에서 실행되는 작은 실행 단위
      스레드는 같은 프로세스 내에서 실행되기 때문에, 프로세스의 자원(메모리 등)을 공유, 자원 공유가 간단하고 빠르다는 장점
프로세스: 독립적인 실행 환경을 제공하는 프로그램의 인스턴스
        프로세스는 독립적인 실행 환경을 가지기 때문에, 자원 공유는 복잡하고 안전한 방법
        메시지 큐, 파일, 소켓 등 다양한 방법 으로 사용

# RTSP 주소를 통해 영상 출력 완료
# 해당 영상을 HTML에 표시하기
http://wandlab.com/blog/?p=94
flask는 Python에서 미들웨어 서버를 구성하게 하는 마이크로 서버 입니다.

# 설치 목록
pip freeze
pip list

# 설치 항목 가져오기
pip freeze > requirements.txt

# flask 라이브러리를 이용한 애플리케이션

# This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. 
# 플라스크 서버가 개발 모드로 실행

# 에러 발생 jinja2.exceptions.TemplateNotFound: index.html
# flask를 사용시 반드시 /templates/를 넣어야 한다.

# 화면 표시 완료
# 새로고침 후 에러발생 malloc: *** error for object 0x2000000000000000: pointer being freed was not allocated
Python에서는 가비지 컬렉터가 자동으로 메모리를 관리하므로 메모리 누수나 메모리 해제 문제에 대해 직접 걱정할 필요가 없다.

# 에러 발생
[h264 @ 0x7f7e5c98be00] out of range intra chroma pred mode
[h264 @ 0x7f7e5c98be00] error while decoding MB 7 7
PC1, PC2에서 동시에 스트림을 진행한 결과 에러 발생
H.264 비디오 스트림을 디코딩하는 동안 문제 발생
해결방법
    1. 최신버전 업그레이드
        pip install --upgrade opencv-python
    2. 스트림의 해상도, 프레임 레이트, 인코딩 설정 확인
    3. 기타 옵션 추가
        cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
    4. 

# python 중간 종료
exit()

# 일반적인 프레임
success, frame = cap.read()

# 다음 프레임 가져오기
cap.grab()  # 버퍼에서 다음 프레임을 가져옴
success, frame = cap.retrieve()  # 실제 프레임을 얻어옴

# 스트리밍 성능 향상
1. 비동기 처리
2. 캡처 및 인코딩 성능 향상
    cv2.VideoCapture는 곧 하드웨어 가속을 사용한다.
    cap = cv2.VideoCapture(rtsp_url1, cv2.CAP_GSTREAMER)
3. 프레임 크기 조절
    frame = cv2.resize(frame, (new_width, new_height))
4. 프레임 압축
    ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, compression_level])

# 테스트
1. fastapi사용결과 성능이 더 악화됨
2. frame size 변경
    frame = cv2.resize(frame, (f_width, f_height))
3. 이미지 품질과 파일 크기 간의 균형 ( 0 ~ 100 )
    ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, compression_level])
4. 혹시나 하는 생각으로 png 용량이 작은 이미지로 변경했지만 영상이 너무 느리게 보여진다.
5. error while decoding MB 14 16, bytestream -9 비디오 프레임을 디코딩하는 동안 문제가 발생했음을 나타냄
