import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

# GPIO setup
MOTOR_PIN = 18
LED_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize camera
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define yellow range
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])

    # Define blue range
    blue_lower = np.array([100, 150, 0])
    blue_upper = np.array([140, 255, 255])

    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

    if cv2.countNonZero(yellow_mask) > 500:
        return 'yellow'
    elif cv2.countNonZero(blue_mask) > 500:
        return 'blue'
    else:
        return 'none'

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        color = detect_color(frame)

        if color == 'yellow':
            GPIO.output(MOTOR_PIN, GPIO.HIGH)
            GPIO.output(LED_PIN, GPIO.LOW)
            print("Yellow object detected – Motor ON")

        elif color == 'blue':
            GPIO.output(MOTOR_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Blue object detected – Motor OFF, LED ON")

        else:
            GPIO.output(MOTOR_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.LOW)
            print("No target color – System idle")

        # Show camera feed for debugging (optional)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
