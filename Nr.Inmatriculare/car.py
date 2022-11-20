
import cv2
import imutils
import numpy
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd = r"D:\tes\tessaract\tesseract.exe"

 
img = cv2.imread(r".\car.jpg")
img = cv2.resize(img, (800, 600))
 
# cv2.imshow("Imagine redimensionata", img)
# cv2.waitKey(0)
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Imagine cu filtru gri", gray)
 
edged = cv2.Canny(gray, 30, 200)
contur = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contur = imutils.grab_contours(contur)
contur = sorted(contur, key = cv2.contourArea, reverse = True)[:10]
 
screenCnt = None
 
for c in contur:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break
 
if screenCnt is None:
    detected = 0
    print("nu a fost detectat niciun contur")
else:
    detected = 1
 
mask = numpy.zeros(gray.shape, numpy.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1,)
new_image = cv2.bitwise_and(img, img, mask=mask)
 
(x, y) = numpy.where(mask == 255)
(topx, topy) = (numpy.min(x), numpy.min(y))
(bottomx, bottomy) = (numpy.max(x), numpy.max(y))
 
CROP = gray[topx:bottomx+1, topy:bottomy+1]
text_numar = pytesseract.image_to_string(CROP, config='--psm 10')
img = cv2.resize(img, (500, 300))
CROP = cv2.resize(CROP, (400, 200))
 
cv2.imshow("CROP", CROP)
 
cv2.waitKey(0)
cv2.destroyAllWindows()