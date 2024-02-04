# import threading
#
# import cv2
# from deepface import DeepFace
#
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 488)
#
# counter = 0
#
# face_match = False
#
# reference_img = cv2.imread(r"C:\Users\nill\Desktop\pf\face-rec\r_img\pp.jpg")
#
#
# def check_face():
#     global face_match
#
#     models = [
#         "VGG-Face",
#         "Facenet",
#         "Facenet512",
#         "OpenFace",
#         "DeepFace",
#         "DeepID",
#         "ArcFace",
#         "Dlib",
#         "SFace",
#     ]
#
#     backends = [
#         'opencv',
#         'ssd',
#         'dlib',
#         'mtcnn',
#         'retinaface',
#         'mediapipe',
#         'yolov8',
#         'yunet',
#         'fastmtcnn',
#     ]
#
#
#
#
#     try:
#         if DeepFace.verify(frame,reference_img.copy(),model_name = models[4],detector_backend = backends[4])['verified']:
#             face_match=True
#         else:
#             print("38")
#             face_match=False
#     except ValueError:
#         face_match=False
#
#
# while True:
#     ret, frame = cap.read()
#
#     if ret:
#         if counter % 100 == 0:
#             try:
#                 threading.Thread(target=check_face(), args=(frame.copy(),)).start()
#             except ValueError:
#                 pass
#         counter += 1
#
#         if face_match:
#             cv2.putText(frame,"MATCHED",(20,450), cv2.FONT_HERSHEY_TRIPLEX,2,(0,255,0),3)
#         else:
#             cv2.putText(frame, "NOT MATCHED", (20, 450), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255), 3)
#
#         cv2.imshow("video",frame)
#
#
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break
#
# cv2.destroyAllWindows()


# ********************************************************************************************************************************


# from deepface import DeepFace

# backends = [
#   'opencv',
#   'ssd',
#   'dlib',
#   'mtcnn',
#   'retinaface',
#   'mediapipe',
#   'yolov8',
#   'yunet',
#   'fastmtcnn',
# ]
# face_objs = DeepFace.extract_faces(img_path = img_p,
#         target_size = (224, 224),
#         detector_backend = backends[4]
# )
# print((face_objs))
# original_image = cv2.imread(img_p)

# # Draw rectangles around the detected faces
# for face_obj in face_objs:
#     x, y, w, h = face_obj['facial_area']['x'], face_obj['facial_area']['y'], face_obj['facial_area']['w'], face_obj['facial_area']['h']

#     cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Display the image with rectangles around detected faces
# cv2.imshow('Detected Faces', original_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# demography = DeepFace.analyze("taken_picture.png")
# print(demography)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


import os
import cv2
from deepface import DeepFace

current_dir = os.getcwd()

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "taken_picture.png"
        cv2.imwrite(os.path.join(f"{current_dir}/t_img/",img_name), frame)
        print(img_name)

        break

cam.release()
cv2.destroyAllWindows()




rf_img = f"{current_dir}/r_img/anindha.jpeg"
t_img = f"{current_dir}/t_img/taken_picture.png"
backends = [
    'opencv',
    'ssd',
    'dlib',
    'mtcnn',
    'retinaface',
    'mediapipe',
    'yolov8',
    'yunet',
    'fastmtcnn',
]
models = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    "DeepFace",
    "DeepID",
    "ArcFace",
    "Dlib",
    "SFace",
]
t_i = cv2.imread(t_img)
original_image = cv2.imread(t_img)
try:
    embedding_t_img= DeepFace.represent(img_path=t_img,
                                      detector_backend=backends[4]
                                      )
    a=[]
    for e_t_img in embedding_t_img:
        # print(e_re_imf)
        a.append(e_t_img)
    print("193",len(a))

    for face_obj in embedding_t_img:
        x, y, w, h = face_obj['facial_area']['x'], face_obj['facial_area']['y'], face_obj['facial_area']['w'], \
            face_obj['facial_area']['h']

        cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if len(a)==1:
        d_w_t= "single face detected"
        cv2.putText(original_image, d_w_t, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow('Face', original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        try:
            result = DeepFace.verify(img1_path=rf_img, img2_path=t_img, model_name=models[0], detector_backend=backends[4])
            print(result)
            if result['verified'] is True:
                cv2.putText(t_i, f"{result['verified']}", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
                cv2.imshow(f"{result['verified']}", t_i)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                cv2.putText(t_i, f"{result['verified']}", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                cv2.imshow(f"{result['verified']}", t_i)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        except ValueError:
            cv2.putText(t_i, "no face detected", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.imshow("No face detected", t_i)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        d_w_t = "multiple face detected"
        cv2.putText(original_image, d_w_t, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow('Face', original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


except ValueError:
    cv2.putText(t_i, "no face detected", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv2.imshow("No face detected", t_i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# print(embedding_objs)




# try:
#     result = DeepFace.verify(img1_path = rf_img, img2_path =t_img,model_name = models[4],detector_backend = backends[4])
#     print(result)
#     if result['verified'] == True:
#         cv2.putText(t_i, f"{result['verified']}", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
#         cv2.imshow(f"{result['verified']}", t_i)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     else:
#         cv2.putText(t_i, f"{result['verified']}", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)
#         cv2.imshow(f"{result['verified']}", t_i)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
# except ValueError:
#     print("not matched")

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# import cv2
# from deepface import DeepFace
# import threading


# cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

# counter= 0
# face_match=False

# reference_img=cv2.imread("taken_picture1.png")

# def check_face(frame):
#     global face_match
#     try:
#         if DeepFace.verify(frame,reference_img.copy())['verified']:

#             face_match=True
#         else:
#             print("63")
#             face_match=False
#     except ValueError:
#         pass


# while True:
#     ret,frame=cap.read()

#     if ret:
#         if counter % 30 == 0:
#             try:
#                 threading.Thread(target=check_face,args=(frame.copy(),)).start()

#             except ValueError:
#                 print("78")
#                 cv2.putText(frame,"NOT matched",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)

#         counter+=1

#         if face_match:
#             cv2.putText(frame,"matched",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
#         else:

#             cv2.putText(frame,"NOT matched",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)

#         cv2.imshow("VIDEO",frame)

#     key=cv2.waitKey(1)

#     if key == ord('q'):
#         break


# cv2.destroyAllWindows()
