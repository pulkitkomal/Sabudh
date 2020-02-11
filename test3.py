import cv2
import numpy as np

imga = cv2.imread('/home/pulkit/PycharmProjects/Sabudh/a.jpg')
#img_ = cv2.resize(img_, (0,0), fx=1, fy=1)
img1 = cv2.cvtColor(imga,cv2.COLOR_BGR2GRAY)

img = cv2.imread('/home/pulkit/PycharmProjects/Sabudh/b.jpg')
#img = cv2.resize(img, (0,0), fx=1, fy=1)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
# find the key points and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
#cv2.imshow('original_image_left_keypoints',cv2.drawKeypoints(img_,kp1,None))


#FLANN_INDEX_KDTREE = 0
#index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
#search_params = dict(checks = 50)
#match = cv2.FlannBasedMatcher(index_params, search_params)
match = cv2.BFMatcher()
matches = match.knnMatch(des1,des2,k=2)


good = []
for m,n in matches:
    if m.distance < 0.03*n.distance:
        good.append(m)


draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   flags = 2)

img3 = cv2.drawMatches(img_,kp1,img,kp2,good,None,**draw_params)
cv2.imwrite("original_image_draMatches.jpg", img3)
cv2.imshow("original_image_drawMatches.jpg", img3)
cv2.waitKey(30000)