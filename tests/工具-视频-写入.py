
import cv2

videoCapture = cv2.VideoCapture('./ignorefiles/001.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # 256M
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 256M

output_video = cv2.VideoWriter('./ignorefiles/divx.mp4', fourcc, fps, size)
 
print(fps, size,'v->',output_video)
 
success, frame = videoCapture.read()
 
while success:
	cv2.imshow('MyWindow', frame)
	cv2.waitKey(1000//int(fps))
	output_video.write(frame)
	success, frame = videoCapture.read()
