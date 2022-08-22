import torch
from matplotlib import pyplot as plt
import numpy as np
from cv2 import waitKey, destroyAllWindows, imshow, VideoCapture, rectangle
import time
import ctypes
import pyautogui
import pygame

# Model
model = torch.hub.load('E:/colab/yolov5','custom', path='E:/colab/yolov5/runs/train/result_test_05_04/weights/best.pt',
source='local')  # local repo

model.conf = 0.85

cap1 = VideoCapture(0)
cap2 = VideoCapture(1)

pygame.mixer.init()      

#다음 알림음은 CLOVA Dubbing으로 제작한 AI 보이스 입니다.                                                                        
warnS1 = pygame.mixer.Sound("알림1.wav")
warnS2 = pygame.mixer.Sound("알림2.wav")


while True:
    time.sleep(0)
    ret, img = cap1.read()
    result = model(img, size=640)
    repos = result.xyxy[0]
    for i in range(len(repos)):
        pos = repos[i].detach()
        rectangle(img, (int(pos[0]), int(pos[1])), (int(pos[2]), int(pos[3])), (255, 255, 255), 2)
    if len(repos) > 0:
        time.sleep(2)
        warnS1.play()
        #ctypes.windll.user32.MessageBoxW(0, "유해동물 탐지 되었습니다.", "경고! 유해동물 탐지", 1)

    imshow('YOLO', np.squeeze(result.render()))
    if waitKey(1) & 0xFF == ord("q"):
        destroyAllWindows()
        break

    ret1, img1 = cap2.read()
    result1 = model(img1, size=640)
    repos1 = result1.xyxy[0]
    for i in range(len(repos1)):
        pos1 = repos1[i].detach()
        rectangle(img1, (int(pos1[0]), int(pos1[1])), (int(pos1[2]), int(pos1[3])), (255, 255, 255), 2)
    if len(repos1) > 0:
        time.sleep(2)
        warnS2.play()
        #ctypes.windll.user32.MessageBoxW(0, "유해동물 탐지 되었습니다.", "경고! 유해동물 탐지", 1)

    imshow('YOLO1', np.squeeze(result1.render()))
    if waitKey(1) & 0xFF == ord("q"):
        destroyAllWindows()
        break    

