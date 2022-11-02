import cv2 # opencv
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
VIDEOS_PATH = 'Tensorflow/workspace/videos'
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

if not os.path.exists(IMAGES_PATH):
    os.mkdir(IMAGES_PATH)

# 노트북에 웹캠이 달려있을 경우
# for label in labels:
#     #  경로 없으면 생성
#     if os.path.exists(IMAGES_PATH+'\\'+label):
#         os.mkdir(IMAGES_PATH+'\\'+label)
#
#     # 5초에 한번씩 비디오 캡쳐해서 라벨 저장
#     cap = cv2.VideoCapture(0)
#     print('Collecting images for {}'.format(label))
#     # time.sleep(5)
#     for imgnum in range(number_imgs):
#         ret, frame = cap.read()
#         imgname = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
#         cv2.imwrite(imgname, frame)
#         cv2.imshow('frame', frame)
#         time.sleep(2)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()


# 미리 촬영해놓은 동영상에서 캡쳐하는 경우
for label in labels:
    #  경로 없으면 생성
    if not os.path.exists(IMAGES_PATH+'\\'+label):
        os.mkdir(IMAGES_PATH+'\\'+label)

    # 5초에 한번씩 비디오 캡쳐해서 라벨 저장
    cap = cv2.VideoCapture(VIDEOS_PATH+'/'+label+'.mp4')
    print('Collecting images for {}'.format(label))
    # time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()