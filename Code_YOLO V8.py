import cv2
import RPi.GPIO as GPIO
from ultralytics import YOLO
import time

# GPIO setup
MOTOR_PIN = 18
LED_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

# Load YOLOv8 model
model = YOLO("your_custom_model.pt")  # Replace with your actual model

# Class ID mapping (based on your model's training)
APPLE_ID = 0    # <-- Replace with actual class ID for 'apple'
ORANGE_ID = 1   # <-- Replace with actual class ID for 'orange'

# Initialize camera
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]

        detected_apple = False
        detected_orange = False

        for box in results.boxes:
            class_id = int(box.cls[0])

            if class_id == APPLE_ID:
                detected_apple = True
            elif class_id == ORANGE_ID:
                detected_orange = True

        # Apply logic: if both detected, orange takes priority
        if detected_orange:
            GPIO.output(MOTOR_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Orange detected – Motor OFF, LED ON")
        elif detected_apple:
            GPIO.output(MOTOR_PIN, GPIO.HIGH)
            GPIO.output(LED_PIN, GPIO.LOW)
            print("Apple detected – Motor ON")
        else:
            GPIO.output(MOTOR_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.LOW)
            print("No target object – Idle")

        # Show frame (optional)
        cv2.imshow("YOLO Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
