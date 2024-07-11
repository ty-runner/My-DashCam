import time
import picamera

with picamera.PiCamera() as camera:
	camera.start_preview()
	time.sleep(2)
	camera.capture('test_image.jpg')
	camera.stop_preview()
