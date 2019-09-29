import numpy as np
#import imutils
import cv2
import os
import time

print("[INFO] loading face detector...")
protoPath = os.path.sep.join(["face_detection_model", "deploy.prototxt"])
modelPath = os.path.sep.join(["face_detection_model",
	"res10_300x300_ssd_iter_140000.caffemodel"])
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
prevTime = 0
cap = cv2.VideoCapture(0)
while True:
	curTime = time.time()
	ret, frame = cap.read()
	frame= cv2.resize(frame, dsize=(500,500),interpolation=cv2.INTER_AREA)
	(h, w) = frame.shape[:2]
	imageBlob = cv2.dnn.blobFromImage(
		cv2.resize(frame, (300, 300)), 1.0, (300, 300),
		(104.0, 177.0, 123.0), swapRB=False, crop=False)
	detector.setInput(imageBlob)
	detections = detector.forward()

	if len(detections) > 0:
		i = np.argmax(detections[0, 0, :, 2])
		confidence = detections[0, 0, i, 2]

		if confidence > 0.6:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			face = frame[startY:endY, startX:endX]
			(fH, fW) = face.shape[:2]
			if fW < 20 or fH < 20:
				continue
			cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 1)
			cv2.imwrite('image.jpg',frame)
        		sec = curTime - prevTime
			prevTime = curTime
			fps = 1/(sec)
			str_fps = "FPS : %0.1f" % fps
			print str_fps
#        cv2.putText(frame, str_fps, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
#	cv2.imshow("Image", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break
		
cap.release()
#cv2.destroyAllWindows()
