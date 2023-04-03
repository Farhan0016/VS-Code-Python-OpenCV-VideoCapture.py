import cv2 as cv

# Read the video from camera===========================================================================
# capture = cv.VideoCapture(0)

# if not capture.isOpened():
#     print("Cannot open camera")
#     exit()

# while True:
#     # Capture frame-by-frame
#     ret, frame = capture.read()

#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     # # Our operations on the frame come here
#     # flip = cv.flip(frame, 0)
#     # cv.imshow("Flipped_Camera", flip)

#     # Display the frame
#     cv.imshow("Camera", frame)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# capture.release()
# cv.destroyAllWindows()
#===================================================================================================

# Read the video from videos
# cap = cv.VideoCapture('./videos/meeting.mp4')

# # This is optional if you want
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# while cap.isOpened():
#     ret, frame = cap.read()

#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.resize(frame, (700, 500), interpolation=cv.INTER_CUBIC)
#     # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     canny = cv.Canny(frame, 125, 175)
#     cv.imshow("Gray", canny)
#     if cv.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()
#=================================================================================================

# # Write Video captured from camera==============================================================
# cap = cv.VideoCapture(0)

# # Define the codec and create VideoWriter object
# # fourcc = cv.VideoWriter_fourcc(*'MJPG')
# """
# A FourCC ("four-character code") is a sequence of four bytes (typically ASCII) used to uniquely identify data formats.
# """
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('./videos/camera.avi', fourcc, 20.0, (640, 480))

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     # flip the frame
#     frame = cv.flip(frame, 0)

#     # write the flipped frame
#     out.write(frame)
#     cv.imshow('Camera', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# cap.release()
# out.release()
# cv.destroyAllWindows()
#================================================================================================

# Write video captured from video clip
cap = cv.VideoCapture('./videos/bees.mp4')
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('./videos/bees_recorded.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.resize(frame, (640, 480), interpolation=cv.INTER_CUBIC)
    out.write(frame)
    cv.imshow("Bees", frame)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
out.release()
cv.destroyAllWindows()