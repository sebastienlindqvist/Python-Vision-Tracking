# this code is for selecting a region of interest (ROI) and then tracking it
#********************************************************************************************
# Import libraries
import cv2
from matplotlib.pyplot import draw
from matplotlib.transforms import Bbox
#********************************************************************************************
# write functions here

def DrawBox(frame, Bbox):
    x, y, w, h = int(Bbox[0]), int(Bbox[1]), int(Bbox[2]), int(Bbox[3])
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, "Tracking", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)



#********************************************************************************************
def main():
    #************************************************************************************
    # Write code here

    #CSRT, KCF, MIL, MOSSE, TLD
    #tracker = cv2.legacy.TrackerMOSSE_create()
    tracker = cv2.TrackerCSRT_create()
    _, frame = cap.read()
    Bbox = cv2.selectROI("Tracking", frame, False)
    tracker.init(frame, Bbox)



    #************************************************************************************
    while True:
        # fps
        timer = cv2.getTickCount()
        # Read image
        _, frame = cap.read()
        #************************************************************************************
        # Write code here
        success, Bbox = tracker.update(frame)

        if success:
            DrawBox(frame, Bbox)
        else:
            cv2.putText(frame, "Tracking lost", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)




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