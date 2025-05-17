# Color-Based Object Detection Using Raspberry Pi with Stepper Motor

## 👨‍💻 Author
- Arunbalaji M (21BEC2141)

---

## 🧠 Overview

This project showcases a real-time color-based object detection system using a Raspberry Pi, camera module, stepper motor, and LED interface. It leverages OpenCV for color detection and integrates hardware components for dynamic interaction based on the detected object color.

---

## 🎯 Objectives

- Detect objects by color using the Raspberry Pi camera and OpenCV.
- Trigger hardware responses (e.g., motor movement, LED alert) based on color classification.
- Create a real-time automation system suitable for applications like surveillance and manufacturing.

---

## 🧩 Features

- 🎥 Real-time color detection using OpenCV and Raspberry Pi camera.
- 🌀 Stepper motor controlled in response to specific object colors.
- 💡 LED indicator for alert scenarios.
- 🔧 HSV and RGB color space manipulation for accurate detection.
- ⚙️ Integration of computer vision with electromechanical control.

---

## 🛠️ Hardware Components

- Raspberry Pi 3B
- RPi Camera Module
- Stepper Motor
- Voltage Booster (CN6009 4A)
- LED and Resistors
- Connecting Wires

---

## 💻 Software Stack

- **Language**: Python
- **Libraries**: `OpenCV`, `RPi.GPIO`, `time`, `numpy`

---

## ⚙️ System Workflow

1. Raspberry Pi camera captures real-time images.
2. OpenCV analyzes color in HSV and RGB color spaces.
3. Based on detected color:
   - Yellow → Stepper motor is activated.
   - Blue → LED glows to indicate an error or anomaly.
4. System provides continuous color-based monitoring and sorting.

---

## 🔄 Circuit Description

- Camera connects via CSI port to Raspberry Pi.
- Stepper motor is controlled via GPIO through a motor driver.
- LED is connected to a GPIO pin with a limiting resistor.
- Voltage booster ensures appropriate power supply to components.

---

## 📷 Output Snapshots

- **Yellow Object Detected** → Motor action triggered.
- **Blue Object Detected** → Red LED activated.

---

## ✅ Result & Conclusion

This project successfully demonstrates a real-time color-based object detection and mechanical actuation system. With the integration of OpenCV and Raspberry Pi hardware, it provides a robust and scalable prototype for smart automation systems in manufacturing, security, and object sorting applications.

---

## 🔮 Future Enhancements

- Add shape detection using edge detection algorithms.
- Incorporate more color classes with adaptive thresholds.
- Expand to robotic arms with multi-axis movement.
- Improve speed and power efficiency with better hardware control.

---

## 📚 References

1. [Computer Vision-Based System for Classification and Sorting Colour Objects](https://iopscience.iop.org/article/10.1088/1757-899X/745/1/012030/meta)  
2. [Conveyor Belt Object Identification](https://digitalcommons.aaru.edu.jo/cgi/viewcontent.cgi?article=3435&context=amis)

---
