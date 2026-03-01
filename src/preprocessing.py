import re
from underthesea import word_tokenize
import pandas as pd
import os

# Danh sách stopwords tiếng Việt cơ bản (Có thể mở rộng thêm)
# Hoặc tải file vietnamese-stopwords.txt từ repo
VIETNAMESE_STOPWORDS = {
    "và", "của", "là", "các", "có", "để", "những", "cho", "trong", "một", 
    "với", "không", "thì", "đã", "được", "người", "khi", "về", "như", "này",
    "đến", "từ", "tại", "vào", "ra", "làm", "rằng", "bị", "hay", "lại",
    "đang", "sẽ", "còn", "cũng", "đều", "rất", "hơn", "nhưng"
}

def clean_text(text):
    """
    Tiền xử lý văn bản tiếng Việt.
    - Lowercasing
    - Loại bỏ ký tự đặc biệt, số, dấu câu
    - Tokenization
    - Xóa Stopwords
    """
    if not isinstance(text, str):
        return ""

    # 1. Lowercasing
    text = text.lower()
    
    # 2. Xóa ký tự đặc biệt, số, giữ lại chữ cái và khoảng trắng
    # Trong tiếng Việt cần chú ý giữ lại các ký tự có dấu
    text = re.sub(r'[^\w\s\ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    
    # Xóa khoảng trắng thừa
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 3. Tokenization (Phân mảnh từ tiếng Việt)
    tokens = word_tokenize(text, format="text").split(" ")
    
    # 4. Remove Stopwords
    tokens = [token for token in tokens if token not in VIETNAMESE_STOPWORDS and token.strip() != ""]
    
    # Gộp lại thành câu trả về
    return " ".join(tokens)

def preprocess_dataset(input_path, output_path):
    """
    Đọc dữ liệu, áp dụng hàm clean_text, lưu ra file mới.
    """
    print(f"Reading data from {input_path}...")
    df = pd.read_csv(input_path)
    
    print(f"Preprocessing {len(df)} rows...")
    df['clean_text'] = df['text'].apply(clean_text)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    raw_path = os.path.join("data", "raw", "vietnamese_news.csv")
    processed_path = os.path.join("data", "processed", "vietnamese_news_cleaned.csv")
    
    if os.path.exists(raw_path):
        preprocess_dataset(raw_path, processed_path)
    else:
        print(f"Error: {raw_path} not found. Please run data_downloader.py first.")
