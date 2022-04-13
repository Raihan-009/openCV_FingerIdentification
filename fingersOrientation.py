import cv2
import handTracker as ht

class FingerOrientation():
    def __init__(self):
        self.tipIds = [4,8,12,16,20]

    def fingerOrientation(self,myhand):
    
        hand_type = myhand['hand_type']
        finger_landmarks = myhand['landmarksList']

        if myhand:
            finger_orientation = []
            if hand_type == "Right Hand":
                if finger_landmarks[self.tipIds[0]][1] > finger_landmarks[self.tipIds[0]-1][1]:
                    finger_orientation.append(1)
                else:
                    finger_orientation.append(0)
            else:
                if finger_landmarks[self.tipIds[0]][1] < finger_landmarks[self.tipIds[0]-1][1]:
                    finger_orientation.append(1)
                else:
                    finger_orientation.append(0)

            for id in range (1,5):
                if finger_landmarks[self.tipIds[id]][2] < finger_landmarks[self.tipIds[id]-2][2]:
                    finger_orientation.append(1)
                else:
                    finger_orientation.append(0)
        return (finger_orientation)

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    handTracker = ht.handDetector()
    fingerTracker = FingerOrientation()
    while True:
        ret, frame = cam.read()
        if ret:
            hands = handTracker.findHands(frame)
            if hands:
                oneHand = hands[0]
                finger_1 = fingerTracker.fingerOrientation(oneHand)

                if len(hands) == 2:
                    seconHand = hands[1]
                    fingers_2 = fingerTracker.fingerOrientation(seconHand)
                    print(finger_1,fingers_2)
                else:
                    print(finger_1)

            cv2.imshow("Framing", frame)
        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()