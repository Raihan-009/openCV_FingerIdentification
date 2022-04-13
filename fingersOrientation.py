import cv2
import handTracker as ht

cam = cv2.VideoCapture(0)
tracker = ht.handDetector()

def fingerOrientation(myhand):
    tipIds = [4,8,12,16,20]
    hand_type = myhand['hand_type']
    finger_landmarks = myhand['landmarksList']
    # return print(hand_type,finger_landmarks)

    if myhand:
        finger_orientation = []
        if hand_type == "Right Hand":
            if finger_landmarks[tipIds[0]][1] > finger_landmarks[tipIds[0]-1][1]:
                finger_orientation.append(1)
            else:
                finger_orientation.append(0)
        else:
            if finger_landmarks[tipIds[0]][1] < finger_landmarks[tipIds[0]-1][1]:
                finger_orientation.append(1)
            else:
                finger_orientation.append(0)

        for id in range (1,5):
            if finger_landmarks[tipIds[id]][2] < finger_landmarks[tipIds[id]-2][2]:
                finger_orientation.append(1)
            else:
                finger_orientation.append(0)
    return (finger_orientation)


while True:
    ret, frame = cam.read()
    if ret:
        hands = tracker.findHands(frame)
        if hands:
            handOne = hands[0]
            finger_1 = fingerOrientation(handOne)

            if len(hands) == 2:
                handTwo = hands[1]
                fingers_2 = fingerOrientation(handTwo)
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
