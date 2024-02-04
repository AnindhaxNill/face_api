

import os
from deepface import DeepFace



def f_a(r_img):
    # rf_img = os.path.join(current_dir,r_img.split('/media/')[1])
    current_dir = os.getcwd()
    r=r_img
    print()
    rf_img = f"{current_dir}{r}"
    t_img = f"{current_dir}/t_img/taken_picture.png"
    print (rf_img)
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

    try:
        embedding_rf_img= DeepFace.represent(img_path=rf_img,detector_backend=backends[4])
        a=[]
        for e_rf_img in embedding_rf_img:
            # print(e_rf_img)
            a.append(e_rf_img)
        if len(a)==1:
            d_w_t= "single face detected"
            # try:
            #     result = DeepFace.verify(img1_path=rf_img, img2_path=rf_img, model_name=models[0], detector_backend=backends[4])
            #     d_w_t=result
            
            # except ValueError:
            #         d_w_t= "no face detected 1 "
        else:
            d_w_t = "multiple face detected"
        
    except ValueError:
        d_w_t="no face detected"

    return d_w_t


