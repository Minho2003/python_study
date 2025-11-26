from paddleocr import PaddleOCR

ocr = PaddleOCR(
    det=True,
    rec=False,
    text_detection_model_name="det_model_name",
    # text_recognition_model_name="rec_model_name",
    det_model_dir="./models/det_model/",
    # rec_model_dir="./models/rec_model/",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
    ) # Switch to PP-OCRv5_mobile models

result = ocr.predict("./general_ocr_002.png")

for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")