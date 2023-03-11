import cv2

# Open the default camera (usually 0)
cap = cv2.VideoCapture(0)

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (640, 480))

# Loop through the frames and record video
while cap.isOpened():
    # Read a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Display the frame (optional)
        cv2.imshow("frame", frame)

        # Write the frame to the output video
        out.write(frame)

        # Check for the "q" key to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()

