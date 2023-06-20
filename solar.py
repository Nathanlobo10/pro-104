import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"sun",(100,80),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"mercury",(110,180),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"venus",(190,270),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"earth",(300,270),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"mars",(400,270),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"jupiter",(500,90),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"saturn",(700,100),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"Uranus",(850,100),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))
cv2.putText(img,"Neptune",(1000,80),cv2.FONT_HERSHEY_SIMPLEX,2,(222,44,89))

cv2.imshow("win",img)
cv2.waitKey(0)


