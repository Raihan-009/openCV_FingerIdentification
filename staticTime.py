import cv2
import handTracker as ht
import fingersOrientation as fo
import fingerIdentification as fi


handTracker = ht.handTracker()
fingerTracker = fo.FingerOrientation()
fingerIdentify = fi.FingerIdentification()


cam = cv2.imread("indexFinger.jpeg")
hands = handTracker.findHands(cam, drawB=True, drawL=False)
if hands:
    oneHand = hands[0]
    finger_1 = fingerTracker.fingerOrientation(oneHand)
    fingerIdentify.fingerIdentification(finger_1)
cv2.imshow("Framing", cam)
cv2.waitKey(0)
cv2.destroyAllWindows()