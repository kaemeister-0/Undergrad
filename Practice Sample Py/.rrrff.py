import numpy as np
import cv2
#create a 512x512 black image
img=np.zeros((512,512,3),np.uint8)
# Draw a rectangle around the text
ori = cv2.rectangle(img,(10,180), (500,300), (0,0,255), 4)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(ori,'Life2Coding',(30,256), font, 2.5,(255,255,255),2,cv2.LINE_AA)
#now use a frame to show it just as displaying a image
cv2.imshow("Text",ori)
cv2.waitKey(0)           
cv2.destroyAllWindows()