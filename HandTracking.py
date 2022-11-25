# Import libraries
import cv2
from matplotlib.pyplot import draw
from matplotlib.transforms import Bbox
import mediapipe as mp
#********************************************************************************************
# write functions here



#********************************************************************************************
def main():
    #************************************************************************************
    # Write code here

    mpHands=mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils



    #************************************************************************************
    while True:
        # fps
        timer = cv2.getTickCount()
        # Read image
        _, frame = cap.read()
        #************************************************************************************
        # Write code here

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results=hands.process(frameRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)



        #************************************************************************************
        # fps
        fps =  cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        # Write fps on frame
        cv2.putText(frame, "FPS: {:d}".format(int(fps)), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        # Display image
        cv2. imshow('Tracking' , frame)
        if cv2.waitKey(10) & 0xFF == ord("q"): 
            break 
    cap.release() 
    cv2.destroyAllWindows() 

#********************************************************************************************
# Run main function
if __name__ == '__main__':
    cap = cv2. VideoCapture(0, cv2.CAP_DSHOW)
    main()