import time
import picamera
from datetime import datetime
from screeninfo import get_monitors
def gen_filename():
	return datetime.now().strftime("%Y-%m-%d_%H-%M-%S.h264")
	
	
with picamera.PiCamera() as camera:
	monitor = get_monitors()[0]
	screen_width = monitor.width
	screen_height = monitor.height
	print(f"Resolution: {screen_width}, {screen_height}")
	camera.rotation=90
	camera.resolution = (screen_width, screen_height)
	camera.start_preview(fullscreen=True)
	#camera.start_preview(fullscreen=False, window=(0,0,400,1200))
	time.sleep(2)
	
	try:
		while True:
			filename = gen_filename()
			camera.start_recording(filename)
			print("Recording... :")
			camera.wait_recording(300)
			camera.stop_recording()
			print("Stopped")
			
	except KeyboardInterrupt:
		camera.stop_recording()
		camera.stop_preview()
		print("Keyboard interrupt")
