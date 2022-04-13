import cv2
import handTracker as ht

cam = cv2.VideoCapture(0)
tracker = ht.handDetector()

while True:
    ret, frame = cam.read()
    if ret:
        hands = tracker.findHands(frame)
        print(hands)
        cv2.imshow("Framing", frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
