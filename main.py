import cv2
import handTracker as ht
import fingersOrientation as fo
import fingerIdentification as fi

cam = cv2.VideoCapture(0)
handTracker = ht.handTracker()
fingerTracker = fo.FingerOrientation()
fingerIdentify = fi.FingerIdentification()
while True:
    ret, frame = cam.read()
    if ret:
        hands = handTracker.findHands(frame)
        if hands:
            oneHand = hands[0]
            finger_1 = fingerTracker.fingerOrientation(oneHand)
            fingerIdentify.fingerIdentification(finger_1)

        cv2.imshow("Framing", frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
