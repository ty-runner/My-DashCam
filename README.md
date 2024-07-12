# My-DashCam
Personal Raspberry Pi (RP4) Dashcam Project to practice CV in Python

## Goal
Create a camera + LCD interface that will accurately record, process, and upload video to a user.

## Usage
1. Download the python file and dependencies at the very least.
2. Create a service file in the raspberry pi's systemd partition: sudo nano /etc/systemd/system/dashcam.service
3. Follow the template in the .service file to create your personalized service file.
4. Reload the kernel daemon: sudo systemctl daemon-reload
5. Enable service on boot: sudo systemctl enable dashcam.service
6. Start the service file: sudo systemctl start dashcam.service
