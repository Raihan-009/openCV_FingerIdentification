import cv2
import handTracker as ht
import fingersOrientation as fo
import fingerIdentification as fi


handTracker = ht.handTracker()
fingerTracker = fo.FingerOrientation()
fingerIdentify = fi.FingerIdentification()

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.rectangle(frame, (10,10), (525,45), (255,255,255), cv2.FILLED)
    cv2.putText(frame, 'Project Finger Identification', (15,35), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
    if ret:
        hands = handTracker.findHands(frame)
        if hands:
            oneHand = hands[0]
            finger_1 = fingerTracker.fingerOrientation(oneHand)
            context = fingerIdentify.fingerIdentification(finger_1)
            print(context)
            cv2.rectangle(frame, (10,50), (325,95), (255,255,255), cv2.FILLED)
            cv2.putText(frame, context, (15,75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,74,186), 2)

        cv2.imshow("Framing", frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


