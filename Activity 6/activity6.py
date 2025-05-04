import cv2
import streamlit as st
import numpy as np
import time

# Setup
st.title("Real-Time Video Stream with OpenCV")
st.sidebar.title("Filter Controls")

# Slider for controlling filter parameters (threshold for edge detection)
threshold1 = st.sidebar.slider("Canny Edge Detection - Threshold 1", 50, 200, 100)
threshold2 = st.sidebar.slider("Canny Edge Detection - Threshold 2", 50, 200, 200)

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Placeholder for displaying the webcam frames
frame_placeholder = st.empty()

# Snapshot button
if st.button("Take Snapshot"):
    ret, frame = cap.read()
    if ret:
        snapshot_filename = f"snapshot_{int(time.time())}.png"
        cv2.imwrite(snapshot_filename, frame)
        st.image(frame, caption="Snapshot Taken", use_container_width=True)
        st.success(f"Snapshot saved as {snapshot_filename}")

# Video stream loop
while True:
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to capture frame")
        break

    # Apply filter: Edge detection using Canny
    edges = cv2.Canny(frame, threshold1, threshold2)

    # Convert edges to BGR for display
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Display the frame with applied filter
    frame_placeholder.image(edges_bgr, channels="BGR", use_container_width=True)

    # Add delay to control the stream speed (useful for smoother display)
    time.sleep(0.05)

# Release the capture when done
cap.release()
