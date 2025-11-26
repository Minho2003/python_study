# OCR Study (PaddleOCR, Tesseract, EasyOCR)

이 폴더는 다양한 OCR 엔진(PaddleOCR / Tesseract / EasyOCR)을 비교·학습하기 위한 공간입니다.

---

## 학습 목표
1. **문서/이미지 인식 정확도 비교**
2. **각 모델의 특징 및 사용 용도 정리**
3. **파인튜닝 연습**

---

## 📂 관련 링크
- [📁 PaddleOCR](https://github.com/Minho2003/python_study/tree/main/OCR/paddleOCR)
- [📁 Tesseract](https://github.com/Minho2003/python_study/tree/main/OCR/Tesseract)
- [📁 EasyOCR](https://github.com/Minho2003/python_study/tree/main/OCR/easyOCR)

---

## 폴더 구조
```
paddleOCR/
├── config/                 # 학습 설정(YAML) 저장
│   ├── config_det.yml
│   ├── config_det_hard.yml
│   └── ...
│
├── data/                   # 학습 및 검증 데이터
│   ├── train/
│   │   ├── images/
│   │   └── det_label.txt
│   └── val/
│       ├── images/
│       └── det_label.txt
│
├── models/                 # export_model 결과 (추론 모델)
│   ├── det_model/
│   │   ├── inference.pdmodel
│   │   ├── inference.pdiparams
│   │   └── inference.pdiparams.info
│   └── rec_model/ (필요 시)
│
├── my_exps/                # 학습 완료 후 생성되는 체크포인트(best_accuracy)
│
├── paddle_ocr_test.py      # 커스텀 모델 테스트 코드
├── readme.md
└── requirements.txt
```


# PaddleOCR

문서/이미지에서 텍스트를 감지(Detection)하고 인식(Recognition)하는 **올인원 OCR 엔진**입니다.

---

## 설치

### requirements.txt 예시
```
paddleocr

# CPU Version of PaddlePaddle
paddlepaddle==3.0.0 --extra-index-url https://www.paddlepaddle.org.cn/packages/stable/cpu/
```

### CLI 설치 명령어
```
python -m pip install paddlepaddle==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
python -m pip install paddleocr
```

---

## 기본 OCR 실행

### CLI 사용
```
paddleocr ocr \
    -i https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png \
    --use_doc_orientation_classify False \
    --use_doc_unwarping False \
    --use_textline_orientation False
```

### 파이썬 실행
```
python paddle_ocr_test.py
```

---

## 주요 파라미터 설명

| 옵션명 | 설명 |
|--------|------|
| **use_doc_orientation_classify** | 이미지의 방향(0°/180°) 자동 보정 |
| **use_doc_unwarping** | 문서 휘어짐(곡면) 자동 펴기 |
| **use_textline_orientation** | 텍스트 라인의 회전 보정 |
| **model_dir** | 커스텀 모델 디렉토리 경로 |

---

# 모델 학습 (Fine-tuning)

### 학습 시작
```
python tools/train.py -c configs/config_det.yml
```

### 모델 내보내기
```
python tools/export_model.py \
    -c configs/config_det.yml \
    -o Global.pretrained_model=./my_exps/best_accuracy \
       Global.save_inference_dir=./models/det_model/
```

---

# 정리

- PaddleOCR은 detection + recognition + 보정이 모두 포함된 **엔진형 OCR 도구**
- CLI와 YAML 기반 구성으로 빠르게 결과 확인 가능
- 파인튜닝 시 `config.yml` 수정 → `train.py` 실행 → `export_model.py` 순서로 진행