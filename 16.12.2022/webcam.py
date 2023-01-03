import cv2
import keyboard
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

# Set the window name
window_name = "Webcam"

# Create a window with the specified name
cv2.namedWindow(window_name)

while True:
    # Read the next frame
    ret, img = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+w), (0,0,255), 2)

    cv2.imshow(window_name, img)

    # Wait for the user to press a key
    key = cv2.waitKey(1)

    # If the user pressed the 'q' key, break out of the loop
    if key == ord('q'):
        break

cap.release()
cv2.waitKey()
cv2.destroyAllWindows() 