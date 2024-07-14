import time
import picamera
from datetime import datetime
from screeninfo import get_monitors
def gen_filename():
	return datetime.now().strftime("%Y-%m-%d_%H-%M-%S.h264")

def get_speed():
    #will be the gps speed module
    return 50
def get_overlay_text():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    speed = get_speed()
    return f"{current_time} \n {speed} mph"

with picamera.PiCamera() as camera:
	monitor = get_monitors()[0]
	screen_width = monitor.width
	screen_height = monitor.height
	print(f"Resolution: {screen_width}, {screen_height}")
	camera.rotation=90
	camera.resolution = (screen_width, screen_height)
	camera.start_preview(fullscreen=True)
	time.sleep(2)
	
	try:
		while True:
			filename = gen_filename()
			camera.start_recording(filename)
			print("Recording... :")
			start_time = time.time()
			while time.time() - start_time < 300:
				overlay_text = get_overlay_text()
				camera.annotate_text = overlay_text
				time.sleep(1)  
			camera.stop_recording()
			print("Stopped")
			
	except KeyboardInterrupt:
		camera.stop_recording()
		camera.stop_preview()
		print("Keyboard interrupt")


