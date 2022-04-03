import cv2
import os

image_folder = '/home/rajibhasan/Desktop/test_video/removed_bg_frames'
video_name = '/home/rajibhasan/Desktop/test_video/video.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
video = cv2.VideoWriter(video_name, fourcc, 29.97002997002997, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()