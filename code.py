import cv2

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

face_count = 0

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw green rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    
    # Display the face count in the top right corner
    cv2.putText(frame, f"Face Count: {len(faces)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

    # Check for the 'o' key to terminate the code
    key = cv2.waitKey(1)
    if key & 0xFF == ord('o'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

# Display the total number of faces detected
print(f"Total Faces Detected: {len(faces)}")

