import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread(r"C:\Users\arunb\Downloads\njan.jpg")

# Convert to RGB for correct Matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb)
plt.axis("off")
plt.show()

# Save the processed image
cv2.imwrite("output.jpg", image)

# Edge detection
edges = cv2.Canny(image, 100, 200)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection')
plt.show()


# Pose estimation using Mediapipe
import mediapipe as mp
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Pose Estimation', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
