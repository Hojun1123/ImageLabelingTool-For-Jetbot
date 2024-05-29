# ImageLabelingTool-For-Jetbot
젯봇의 Road Following을 위한 이미지 라벨링 도구

### 개발 목적
https://github.com/NVIDIA-AI-IOT/jetbot﻿
NDIVIA에서 Jetbot의 Road Following을 위해 기본으로 제공하는 ImageLabeling 도구는 최소 수백 장의 이미지들을 라벨링하기에는 불편하기 때문에
, 빠른 작업을 위해 개발

### Key Control
- A, D : 이미지 좌우 넘기기(이전/다음 이미지)
- W, S : 라벨링 타입 조작 (Not used), 추후 필요 시 기능 등록하여 사용 가능
  -  만약 키 입력이 되지 않는다면 GUI 라벨을 한 번 클릭 후 사용

### 저장 (작업 완료 후 저장 필)
- Ctrl +S 또는 상단 메뉴 바의 저장 클릭
- 저장 시, /result 폴더가 생성되며, 이미지들이 라벨링되어 저장됨

라벨링할 이미지들의 경로는 기본 값으로 ./images 로 설정됨

![image](https://github.com/Hojun1123/ImageLabelingTool-For-Jetbot/assets/65999992/5c117b43-2a8c-41c3-bad8-2d72b4a26b88)




