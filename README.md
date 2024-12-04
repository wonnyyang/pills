# 알약 인식 인공지능 모델

## 프로젝트 개요
이 프로젝트는 알약을 인식하는 인공지능 모델을 개발하는 것을 목표로 합니다. 이 모델은 치매 환자나 건망증이 심한 사람들을 위한 AI 알약 인식 알람 시스템의 일부로, 사용자가 알람이 울릴 때 알약을 인식하여 알람을 끌 수 있도록 설계되었습니다. 하지만 현재 리포지토리에 올라간 파일은 알약만 인식하는 모델입니다.

## 개발 동기
많은 사람들이 치매나 건망증으로 인해 약 복용을 잊어버리는 경우가 많습니다. 이러한 문제를 해결하기 위해, 알람이 울리면 사용자가 알약의 이미지를 인식시키고 알람을 끌 수 있는 시스템을 개발하게 되었습니다. 이 모델은 사용자의 건강 관리를 지원하고, 약물 복용을 보다 쉽게 만들어 줍니다.

## 기술 스택
- **프로그래밍 언어**: Python
- **딥러닝 프레임워크**: YOLOv5
- **라이브러리**: OpenCV, NumPy, Matplotlib

## 데이터셋
알약 인식 모델은 다양한 알약의 이미지를 포함한 데이터셋을 사용하여 훈련되었습니다. 이 데이터셋은 직접 라벨링한 알약 사진들로 구성되어 있으며, 모델의 정확도를 높이기 위해 다양한 각도와 조명에서 촬영된 이미지를 포함하고 있습니다.

## 설치 방법
1. 이 리포지토리를 클론합니다:
   ```bash
   git clone https://github.com/username/repository.git
   
프로젝트 전반적인 설명:
본 프로젝트는 정해진 시간에 알람이 울리면 사용자의 약 복용 동작을 카메라로 실시간 감지하여 약을 먹으면 알람을 자동으로 해제하는 시스템을 목표로 한다. 이를 위해 CNN 기반 딥러닝 모델을 학습시켜 약 복용 동작을 정확히 식별하도록 설계하였다.

제안하고 싶은 프로젝트의 강점:
사용자의 약 복용 시간 준수를 지원하며, 약 복용 시간을 잊는 것을 방지한다. 실시간 감지 기술을 활용하여 사용 편의성을 높이고 정확한 모니터링을 제공한다.

프로젝트의 중요성:
약 복용은 건강 관리의 핵심 요소로, 시간 준수는 약의 효과에 직접적인 영향을 미친다. 본 시스템은 사용자의 약 복용 습관을 개선하여 건강 유지와 치료 효율성을 높이는 데 기여한다.

직면하고 있는 한계:
약 복용 동작을 다양한 환경에서 정확히 인식하는 데 있어 데이터 부족, 모델의 과적합 가능성, 환경 변화에 대한 민감성 등이 한계로 작용할 수 있다.

문헌고찰:
기존 연구는 주로 정형화된 환경에서 약 복용 동작을 분석하였으나, 본 프로젝트는 실시간 환경에서의 적용 가능성을 목표로 한다. Smith et al.(2020)과 Kim et al.(2019)의 연구를 참고하여 딥러닝 모델 성능을 개선하고자 하였다.





# Pill Recognition AI Model

## Project Overview
This project aims to develop an artificial intelligence model that recognizes pills. This model is part of an AI pill recognition alarm system designed for patients with dementia or severe forgetfulness, allowing users to recognize pills when an alarm goes off to turn it off. However, the files currently uploaded in this repository exclusively focus on recognizing pills.

## Motivation for Development
Many people forget to take their medications due to dementia or forgetfulness. To address this issue, we developed a system that allows users to recognize a pill's image when an alarm rings and turn it off. This model supports users in managing their health and facilitates medication adherence.

## Technology Stack
- **Programming Language**: Python
- **Deep Learning Framework**: YOLOv5
- **Libraries**: OpenCV, NumPy, Matplotlib

## Dataset
The pill recognition model was trained using a dataset containing images of various pills. This dataset consists of pill photos that were labeled manually, including images taken from various angles and lighting conditions to enhance the model's accuracy.

## Installation Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/username/repository.git
   
Project Overview:
This project aims to develop a system where an alarm sounds at designated times, and a real-time camera detects the user's pill-taking motion to automatically deactivate the alarm upon confirmation. A CNN-based deep learning model is trained to accurately identify pill-intake actions.

Proposed Strengths of the Project:
The system helps users adhere to medication schedules, preventing them from forgetting to take their pills. By utilizing real-time detection technology, it enhances user convenience and provides accurate monitoring.

Importance of the Project:
Adherence to medication schedules is critical for effective treatment and overall health management. This system contributes to improving pill-taking habits, promoting better health outcomes and medication efficiency.

Current Challenges:
The project faces challenges such as insufficient data for diverse scenarios, potential overfitting of the model, and sensitivity to environmental changes, which could impact accurate detection.

Literature Review:
Previous studies have primarily focused on analyzing pill-intake actions in controlled environments. This project aims to extend their applicability to real-time settings. The research by Smith et al. (2020) and Kim et al. (2019) was referenced to enhance the performance of the deep learning model.
