import cv2
import dlib
from scipy.spatial import distance
#import face_recognition
import time
from threading import Thread
import numpy as np
import playsound




#from pygame import mixer

#mixer.init()
#soundfile = mixer.Sound('alarm.wav')

MIN_EAR = 0.30
EYE_AR_CONSEC_FRAMES = 30

COUNTER = 0
ALARM_ON = False

def calculate_EAR(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear_aspect_ratio = (A+B)/(2.0*C)
	return ear_aspect_ratio

def sound_alarm(soundfile):
 #   try:
        #soundfile.play()
    playsound.playsound(soundfile)
                
   # except:  # isplaying = False
    #    pass
 

def main():
    global COUNTER,ALARM_ON
    cap = cv2.VideoCapture(0)
    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor("model\\shape_predictor_68_face_landmarks.dat")


    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = hog_face_detector(gray)
        for face in faces:
            x1=face.left()
            y1=face.top()
            x2=face.right()
            y2=face.bottom()
            # Drawing a rectangle around the face
            cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0),3)
            #cv2_imshow(frame)
            face_landmarks = dlib_facelandmark(gray, face)
            
            leftEye = []
            rightEye = []

            for n in range(36,42):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                leftEye.append((x, y))
                next_point = n+1
                if n == 41:
                    next_point = 36
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

            
            for n in range(42,48):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                rightEye.append((x, y))
                next_point = n+1
                if n == 47:
                    next_point = 42
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
                
            left_ear = calculate_EAR(leftEye)
            right_ear = calculate_EAR(rightEye)
            
            EAR = (left_ear+right_ear)/2
            EAR = round(EAR, 2)
            
            lpts = np.array(leftEye)
            rpts = np.array(rightEye)
            
            cv2.polylines(frame,[lpts],True,(255,255,0),1)
            cv2.polylines(frame,[rpts],True,(255,255,0),1)
            
            
            # check to see if the eye aspect ratio is below the blink
		# threshold, and if so, increment the blink frame counter
            if EAR<MIN_EAR:
                COUNTER+=1
                # if the eyes were closed for a sufficient number of
			# then sound the alarm
                if COUNTER>=EYE_AR_CONSEC_FRAMES:
                    if not ALARM_ON:
                        ALARM_ON = True
                        # check to see if an alarm file was supplied,
					# and if so, start a thread to have the alarm
					# sound played in the background
                        t = Thread(target=sound_alarm,args=('alarm.wav',))
                        t.daemon = True
                        t.start()
                #try:
                 #   sound.play()
                
#                except:  # isplaying = False
 #                   pass
                
                cv2.putText(frame,"DROWSINESS DETECTED!!!", (10,30), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
               # cv2.putText(frame,"STOP AND REST!", (20,400), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
            #    print("DROWSY")
            else:
                # otherwise, the eye aspect ratio is not below the blink
		# threshold, so reset the counter and alarm
                COUNTER=0
                ALARM_ON=False
                cv2.putText(frame,"EAR{:.2f}".format(EAR), (300,30), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
             #   print(EAR)
                
        cv2.imshow("DROWSINESS DETECTION!", frame)

        key = cv2.waitKey(1) & 0xFF
        #if the key 'q' for engine keypress' is pressed, break from loop
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    

    
if __name__=='__main__':
    main()
          

