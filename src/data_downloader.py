import os
import pandas as pd
import requests
import zipfile
import io

# URL của một bộ dữ liệu phân loại văn bản tiếng Việt đơn giản (tùy chọn 1)
# Hoặc chúng ta tạo mock dataset để đảm bảo code chạy được trước
def create_mock_vietnamese_news_dataset(output_path):
    print(f"Creating mock dataset at {output_path}...")
    
    data = [
        {"text": "Chính phủ vừa ban hành nghị định mới về phát triển kinh tế số, tập trung vào AI.", "label": "Chính trị"},
        {"text": "Thủ tướng nhấn mạnh tầm quan trọng của việc bảo vệ an ninh mạng trong cuộc họp thường kỳ.", "label": "Chính trị"},
        {"text": "Làn sóng sa thải tại các công ty công nghệ lớn vẫn chưa có dấu hiệu dừng lại.", "label": "Kinh tế"},
        {"text": "Giá vàng hôm nay tiếp tục tăng mạnh do những bất ổn từ thị trường toàn cầu.", "label": "Kinh tế"},
        {"text": "Đội tuyển Việt Nam đã có một trận đấu quả cảm trước đối thủ mạnh tại vòng loại World Cup.", "label": "Thể thao"},
        {"text": "Huấn luyện viên trưởng quyết định thay đổi chiến thuật ở hiệp 2 mang lại hiệu quả cao.", "label": "Thể thao"},
        {"text": "Bộ phim điện ảnh mới ra rạp đã nhanh chóng phá kỷ lục doanh thu phòng vé.", "label": "Giải trí"},
        {"text": "Nam ca sĩ nổi tiếng vừa ra mắt MV mới với mức đầu tư khủng và hình ảnh bắt mắt.", "label": "Giải trí"},
        {"text": "Apple vừa chính thức giới thiệu dòng iPhone mới với nhiều cải tiến về camera và thời lượng pin.", "label": "Công nghệ"},
        {"text": "Mô hình ngôn ngữ lớn ChatGPT đang tạo ra cuộc cách mạng trong lĩnh vực AI sinh tạo.", "label": "Công nghệ"}
    ]
    
    # Nhân bản dữ liệu lên để làm tập test
    data = data * 50 
    
    df = pd.DataFrame(data)
    
    # Tạo thư mục nếu chưa có
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Lưu ra CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Mock dataset created successfully with {len(df)} samples!")

if __name__ == "__main__":
    raw_data_path = os.path.join("data", "raw", "vietnamese_news.csv")
    create_mock_vietnamese_news_dataset(raw_data_path)
