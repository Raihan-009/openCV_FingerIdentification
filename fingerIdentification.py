import cv2
import handTracker as ht
import fingersOrientation as fo

class FingerIdentification():
    def __init__(self):
        pass

    def fingerIdentification(self,orientation):
        if ((orientation.count(1)) == 5):
            print("All Fingers are Tapped")
        elif (orientation[0] == 1):
            print("Thumb Finger Tapped")
        elif (orientation[1] == 1):
            print("Index Finger Tapped")
        elif (orientation[2] == 1):
            print('Middle Finger tapped')
        elif (orientation[3] == 1):
            print("Ring Finger Tapped")
        elif (orientation[4] == 1):
            print("Little Finger Tapped")
        else:
            print("No Finger Tapped")

def main():

    cam = cv2.VideoCapture(0)
    handTracker = ht.handDetector()
    fingerTracker = fo.FingerOrientation()
    fingerIdentify = FingerIdentification()
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

if __name__ == "__main__":
    main()
