import cv2
import re
cv_info = [re.sub('\s+', ' ', ci.strip()) for ci in cv2.getBuildInformation().strip().split('\n') 
               if len(ci) > 0 and re.search(r'(nvidia*:?)|(cuda*:)|(cudnn*:)|(ffmpeg*:?)|(gstreamer*:?)', ci.lower()) is not None]
print(cv_info)
