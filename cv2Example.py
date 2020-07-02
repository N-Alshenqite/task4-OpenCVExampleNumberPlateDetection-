import cv2

minArea = 500
color = (255,0,255)
numberPlatesCasCade = cv2.CascadeClassifier("C:/Users/Nour/PycharmProjects/OpenCVPython/venv/Lib/site-packages/cv2/data/haarcascade_russian_plate_number.xml")
path = "C:/Users/Nour/Desktop/2.jpg"
img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

numberplates = numberPlatesCasCade.detectMultiScale(gray,1.1,4)

for (x,y,w,h)in numberplates:
    area = w*h
    if area > minArea :
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
         cv2.putText(img,"Number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
         imgRoi = img[y:y+h,x:x+w]
         cv2.imshow("ROI",imgRoi)
cv2.imshow("Result",img)
cv2.waitKey(0)