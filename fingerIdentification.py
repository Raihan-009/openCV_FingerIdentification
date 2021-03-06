import cv2
import handTracker as ht
import fingersOrientation as fo

class FingerIdentification():
    def __init__(self):
        pass

    def fingerIdentification(self,orientation):
        if ((orientation.count(1)) == 5):
            #print("All Fingers are showing")
            context = "All Fingers are showing"
            return context
        elif((orientation.count(0)) == 5):
            #print("All Finger Tapped")
            context = "All Finger Tapped"
            return context

        elif ((orientation[0] == 0) & (orientation[1] == 1) & (orientation[2] == 1) & (orientation[3] == 1) & (orientation[4] == 1)):
            #print("Thumb Finger Tapped")
            context = "Thumb Finger Tapped"
            return context
        elif ((orientation[0] == 1) & (orientation[1] == 0) & (orientation[2] == 0) & (orientation[3] == 0) & (orientation[4] == 0)):
            #print("Thumb Finger")
            context = "Thumb Finger"
            return context
        elif ((orientation[0] == 1) & (orientation[1] == 0) & (orientation[2] == 1) & (orientation[3] == 1) & (orientation[4] == 1)):
            #print("Index Finger Tapped")
            context = "Index Finger Tapped"
            return context
        elif ((orientation[0] == 0) & (orientation[1] == 1) & (orientation[2] == 0) & (orientation[3] == 0) & (orientation[4] == 0)):
            #print("Index Finger")
            context = "Index Finger"
            return context
        elif ((orientation[0] == 1) & (orientation[1] == 1) & (orientation[2] == 0) & (orientation[3] == 1) & (orientation[4] == 1)):
            #print("Middle Finger Tapped")
            context = "Middle Finger Tapped"
            return context
        elif ((orientation[0] == 0) & (orientation[1] == 0) & (orientation[2] == 1) & (orientation[3] == 0) & (orientation[4] == 0)):
            #print("Middle Finger")
            context = "Middle Finger"
            return context
        elif ((orientation[0] == 1) & (orientation[1] == 1) & (orientation[2] == 1) & (orientation[3] == 0) & (orientation[4] == 1)):
            #print("Ring Finger Tapped")
            context = "Ring Finger Tapped"
            return context
        elif ((orientation[0] == 0) & (orientation[1] == 0) & (orientation[2] == 0) & (orientation[3] == 1) & (orientation[4] == 0)):
            #print("Ring Finger")
            context = "Ring Finger"
            return context
        elif ((orientation[0] == 1) & (orientation[1] == 1) & (orientation[2] == 1) & (orientation[3] == 1) & (orientation[4] == 0)):
            #print("Little Finger Tapped")
            context = "Little Finger Tapped"
            return context
        elif ((orientation[0] == 0) & (orientation[1] == 0) & (orientation[2] == 0) & (orientation[3] == 0) & (orientation[4] == 1)):
            #print("Little Finger")
            context = "Little Finger"
            return context
        
    

def main():

    cam = cv2.VideoCapture(0)
    handTracker = ht.handTracker()
    fingerTracker = fo.FingerOrientation()
    fingerIdentify = FingerIdentification()
    while True:
        ret, frame = cam.read()
        if ret:
            hands = handTracker.findHands(frame)
            if hands:
                oneHand = hands[0]
                finger_1 = fingerTracker.fingerOrientation(oneHand)
                print(finger_1)
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
