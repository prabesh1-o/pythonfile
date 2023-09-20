import cv2
import mediapipe as md

md_drawing =md.solutions.drawing_utils
md_drawing_styles = md.solutions.drawing_styles
md_pose = md.solutions.pose

count = 0
position = None
cap = cv2.VideoCapture(0)

with md_pose.pose(
    min_detection_cnfidence = 0.7,
    min_tracking_confidence = 0.7) as pose:
    while cap .isOpened():
        sucess,image=cap.read()
        if not sucess:
            print("empty camera")
            break
        
        image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGRRGB)
        result = pose.process(image)
        
        imlist = []
        if result.pose_landmarks:
            md_drawing.draw_landmarks(
                image,result.pose_landmarks,md_pose.pose_connections)
            for id,im in enumerate(result.pose_landmarks.landmarks):
                h,w,_=image.shape
                X,Y=int(im.x*w),int(im.y*h)
                imlist.append([id,X,Y])
        if (imlist[12][2] and imlist[12][2] >= imlist[14][2] and imlist[13][2]):
            position = 'down'
        if(imlist[12][2] and imlist[11][2] <= imlist[14][2] and imlist[13][2]) and position == 'down':
            position='up'
            count+=1
            print(count)
            
        cv2.imshow("push_up counter",cv2.flip(image,1))
        key = cv2.waitKey(1)
        if key==ord('q'):
            break    
    
cap.release()   
    
        



