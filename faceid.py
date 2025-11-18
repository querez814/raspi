import cv2
from picamera2 import Picamera2
from gpiozero import LED
import time

face_cascade = cv2.CascadeClassifier('/home/student2/zaki/haarcascade_frontalface_default.xml')

# LED on GPIO 17
led = LED(17)

# Initialize camera
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"size": (640, 480)}))
camera.start()

time.sleep(2)  

try:
    while True:
        frame = camera.capture_array()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            led.on()
            print("Face detected → LED ON")
        else:
            led.off()
            print("No face → LED OFF")

        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    led.off()
    camera.stop()
    cv2.destroyAllWindows()
