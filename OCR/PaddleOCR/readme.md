# OCR Study (PaddleOCR, Tesseract, EasyOCR)

이 폴더는 다양한 OCR 엔진(PaddleOCR / Tesseract / EasyOCR)을 비교·학습하기 위한 공간입니다.

---

## 학습 목표
1. 문서/이미지 인식 정확도 비교
2. 각 모델의 특징 및 사용 용도 정리
3. 파인튜닝 연습

---

## 📂 관련 링크
- [PaddelOCR](https://github.com/Minho2003/ML_study/tree/main/OCR/PaddleOCR)
- [Tesseract](https://github.com/Minho2003/ML_study/tree/main/OCR/Tesseract)
- [EasyOCR](https://github.com/Minho2003/ML_study/tree/main/OCR/EasyOCR)
---

# 공부한 내용
Paddle OCR은 VLM 모델이다.
end to end 파이프라인으로 Detection + Recognition 모델로 이루어져있다.
Text Detection -> Text

손글씨, 이미지 텍스트 모두 가능하고, 다국어 지원이 되어 활용도가 높다. 

detection 모델에서 이미지가 왜곡되어있거나 글자가 왜곡되어 있어도 인식이 가능하다. 

mobile 모델로 가볍게 사용할수도 있고, fine tuning을 통해 원하는대로 .yml을 수정해 학습시키는 것도 편리하다. 

