# convierte un video a imagenes usando opencv
import cv2
vidcap = cv2.VideoCapture('erupcionYoutube.mp4')
success, image = vidcap.read()
count = 0
while success:
                    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
                    success, image = vidcap.read()
                    count += 1
