# AGENTS.md 

## System Architecture & Workflow (Chi tiết luồng xử lý mới)
- **1. Input Layer (Nhận Link):** API endpoint (vd: dùng FastAPI hoặc Flask) nhận request chứa URL của một bài báo từ người dùng.
- **2. Scraper Agent (Cào dữ liệu):** Sử dụng các thư viện như `BeautifulSoup`, `newspaper3k` hoặc `trafilatura` để truy cập URL và bóc tách nội dung văn bản chính, loại bỏ các thành phần rác (quảng cáo, menu, footer).
- **3. Preprocessor Agent (Tiền xử lý):** Nhận văn bản vừa cào được, tiến hành làm sạch, tách từ tiếng Việt (tokenize bằng `pyvi`, `underthesea`...) và loại bỏ stopword tương tự như khi train.
- **4. Classifier Agent (Phân loại):** Đưa văn bản đã làm sạch qua mô hình AI đã lưu (SVM, LSTM hoặc PhoBERT trong thư mục `models/`) để dự đoán phân lớp (Chính trị, Kinh tế, Thể thao,...).
- **5. Output Layer (Trả nhãn):** Trả về nhãn (label) cuối cùng và độ tin cậy (confidence score) cho người dùng dưới dạng JSON.

## Dev environment tips
- Khởi tạo môi trường với `python -m venv venv` và kích hoạt trước khi code. Cài đặt các thư viện hiện tại bằng `pip install -r requirements.txt`.
- Cài đặt thêm các công cụ hỗ trợ ý tưởng mới: `pip install fastapi uvicorn beautifulsoup4 requests` và nhớ cập nhật lại `requirements.txt`.
- Cấu trúc lại source code: Tạo thêm `src/scraper.py` (chứa logic bóc tách web) và `src/api.py` (chứa logic nhận link và trả nhãn) để không ảnh hưởng đến code training cũ.
- Dùng `uvicorn src.api:app --reload` để khởi chạy server API phục vụ test local thay vì chạy script console.
- Chú ý kiểm tra đường dẫn load file mô hình (`.pkl`, `.pt`) xem đã trỏ đúng vào thư mục `models/` khi khởi động API hay chưa.

## Testing instructions
- Tìm và đặt các kịch bản test trong thư mục `tests/` (nếu chưa có thì tạo mới).
- Chia test ra thành các module nhỏ:
  - Chạy `pytest tests/test_scraper.py` để đảm bảo bot cào đúng text từ các trang báo phổ biến (VNExpress, Dân Trí, Tuổi Trẻ...).
  - Chạy `pytest tests/test_classifier.py` để đảm bảo mô hình vẫn infer (dự đoán) tốt.
  - Chạy `pytest tests/test_api.py` để test toàn bộ luồng: Gửi URL -> Nhận JSON có chứa nhãn.
- Cần xử lý các lỗi ngoại lệ (Edge cases) trong quá trình test: Link chết (404), link không phải bài báo, hoặc web chặn bot.
- Sửa mọi lỗi type error hoặc test failed cho tới khi toàn bộ bộ test đều "xanh" (pass) bằng lệnh `pytest`.

## PR instructions
- Title format: `[DA_XLNNTN] <Tiêu đề tính năng>` (Ví dụ: `[DA_XLNNTN] Thêm luồng crawl báo từ URL`).
- Luôn chạy format code (như `black` hoặc `flake8`) và chạy lệnh `pytest` trước khi tạo commit.
- Cập nhật file `README.md` (đặc biệt là mục ▶️ Running the Project) để người khác biết cách sử dụng hệ thống qua link URL thay vì text tĩnh. Thêm cả test cho những code mới bạn vừa viết, kể cả khi không ai yêu cầu.