import cv2 as cv

img = cv.imread("images.jpg",0)

cv.imshow("images.jpg",img)
k = cv.waitKey(100000) # Wait for a keystroke in the window
cv.destroyAllWindows()