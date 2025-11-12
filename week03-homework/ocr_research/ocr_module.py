from paddleocr import PaddleOCR
from llama_index.core import Document
from pathlib import Path
import logging

class SimpleDirectoryImagesReader:
    """A simple image reader that reads all images from a directory."""

    def __init__(self, input_dir: str):
        self.input_dir = Path(input_dir)

    def load_data(self):
        """Load all images from the directory."""
        strarray = ocr_helper(str(self.input_dir))
        documents = [Document(text=txt) for txt in strarray]
        return documents

def ocr_helper(input_dir: str) -> list[str]:
    """Perform OCR on the given images or all images in the given directory."""
    if input_dir:
        # 初始化 PaddleOCR 实例
        ocr = PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False)

        # 对示例图像执行 OCR 推理 
        result = ocr.predict(
            input=str(input_dir)
        )

        strarray = []

        for res in result:
            strarray.append("".join(res["rec_texts"]))
            res.save_to_img("output")
            res.save_to_json("output")

        logging.info(f'Finish OCR parsing, the text is : {strarray}')
        return strarray

if __name__ == "__main__":
    logging.info("OCR test begin")
    image_path = Path(__file__).parent.parent / "image"
    # ocr_helper(str(image_path))
    documents = SimpleDirectoryImagesReader(image_path).load_data()
    logging.info(f"Loaded documents: {documents}")