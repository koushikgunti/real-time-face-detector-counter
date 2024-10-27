# real-time-face-detector-counter
# Face Detection using OpenCV

This project demonstrates real-time face detection using OpenCV's Haar Cascade Classifier. The application captures video from the webcam and detects faces in the frame, displaying a count of detected faces in real time.

## Requirements

- Python 3.x
- OpenCV
- NumPy (optional, but often needed for image processing)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/koushikgunti/facedetection.git
   cd facedetection

### Install the required packages:
pip install opencv-python
Code Explanation

### code Explanation
  
The script uses OpenCV's CascadeClassifier to load a pre-trained model for face detection.

The webcam is initialized using cv2.VideoCapture(0).

Each frame captured from the webcam is converted to grayscale for processing.

he detectMultiScale function is called to detect faces, and rectangles are drawn around each detected face. The total number of faces 
detected is displayed in real time.
