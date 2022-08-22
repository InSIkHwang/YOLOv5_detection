# YOLOv5_detection
학습한 YOLOv5 커스텀 모델을 불러와 웹캠을 통한 실시간 탐지 시스템 입니다.

## 사용법
* GUI.py를 받은 후, 본인이 적용시킬 .pt 파일의 경로로 수정하셔야 합니다.
```python
# Model
model = torch.hub.load('E:/colab/yolov5','custom', path='E:/colab/yolov5/runs/train/result_test_05_04/weights/best.pt',
source='local')  # local repo
```
* 실행 시 웹캠을 통해 실시간 탐지를 하며 객체 탐지 시 알림음을 재생합니다. (알림음은 CLOVA Dubbing으로 제작한 AI 보이스 입니다. 본인이 원하는 .wav 파일 사용 가능)
* 종료를 원하는 경우 = 'q'
* 객체의 정확도가 85% 이상일 때 알림이 울리게 설정 되어 있음. (수정가능) (model.conf = 0.85)
```python
model.conf = 0.85
```

### 예시
![시연1](https://user-images.githubusercontent.com/85327744/185901917-4adb8c1d-2ada-4b10-91f8-adf6585a3a73.JPG)
![시연4](https://user-images.githubusercontent.com/85327744/185901943-9b268339-86aa-4055-b63c-3f3e7e30fd18.JPG)
