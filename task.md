# Kế hoạch thực hiện dự án NLP Phân loại văn bản

## 1. Cài đặt môi trường và Tải dữ liệu
- [x] Tạo môi trường ảo (virtualenv) và cài đặt các thư viện trong `requirements.txt`.
- [x] Tìm kiếm và thu thập tập dữ liệu phân loại văn bản tiếng Việt.
  - *Nguồn học: VNExpress, Zing hoặc các dataset trên Kaggle.*
  - *Các danh mục cần có: Chính trị, Kinh tế, Thể thao, Giải trí, Công nghệ.*
- [x] Lưu trữ dữ liệu gốc vào `data/raw/`.

## 2. Tiết xử lý dữ liệu (Preprocessing)
- [x] Viết hàm đọc và khám phá nhanh dữ liệu (EDA) trên `notebooks/`. *(Đã kết hợp trong code)*
- [x] Thực hiện tiền xử lý cơ bản trong `src/preprocessing.py`:
  - [x] Chuyển chữ thường (Lowercasing).
  - [x] Xóa các ký tự đặc biệt, dấu câu.
  - [x] Loại bỏ Stopwords (tiếng Việt).
  - [x] Thực hiện Tokenization (sử dụng `underthesea` hoặc `pyvi` để tách từ tiếng Việt).
- [ ] Tùy chọn (Optional): Lemmatization / Stemming.
- [x] Đảm bảo tất cả các bước tiền xử lý có thể tái tạo (reproducible) và lưu dữ liệu đã qua xử lý vào `data/processed/`.

## 3. Trích xuất đặc trưng (Feature Engineering)
- [x] Hiện thực các phương pháp chuyển đổi văn bản thành vector (Vectorization) trong `src/feature_engineering.py`:
  - [x] Bag of Words (CountVectorizer). *(Đã triển khai)*
  - [x] TF-IDF. *(Mặc định)*
  - [ ] Word2Vec hoặc FastText (Tùy chọn cho mô hình nâng cao).
  - [ ] BERT embeddings (PhoBERT) (Tùy chọn nâng cao).

## 4. Xây dựng và Huấn luyện Mô hình (Modeling & Training)
- [x] Chia tách tập dữ liệu: train / validation / test.
- [x] Xây dựng các mô hình cơ bản (Baseline models) trong `src/model.py` và `src/train.py`:
  - [x] Naive Bayes.
  - [x] Logistic Regression.
  - [x] SVM.
  - [x] Random Forest.
- [ ] Thử nghiệm Cross-validation.
- [ ] (Tùy chọn) Xây dựng mô hình nâng cao (Deep Learning): LSTM, CNN for text, PhoBERT.
- [x] Bổ sung tính năng lưu mô hình tốt nhất vào thư mục `models/` sau khi huấn luyện xong.
- [ ] Ghi lại các tham số, số liệu đánh giá (metrics) và lưu trữ lại (Experiment tracking).

## 5. Đánh giá Mô hình (Evaluation)
- [x] Viết script `src/evaluate.py` để tính toán và báo cáo các chỉ số phân tích:
  - [x] Accuracy.
  - [x] Precision, Recall, F1-score (`classification_report`).
  - [x] Confusion Matrix, được thể hiện qua biểu đồ trực quan (lưu trong `reports/`).
- [x] Trực quan hóa đường cong giảm sai số (Loss curve - nếu dùng mô hình DL).
- [x] So sánh hiệu năng của ít nhất 1 mô hình Machine Learning truyền thống và 1 mô hình Deep Learning.

## 6. Lập Báo cáo và Đóng gói (Reporting & Packaging)
- [x] Soạn thảo báo cáo cuối cùng (PDF) vào `reports/`, bao gồm:
  - Tổng quan kiến trúc & các thử nghiệm.
  - So sánh kết quả và phương pháp phân tích lỗi (Error analysis).
  - Các biểu đồ thống kê, so sánh.
- [x] Review lại mã nguồn đảm bảo tuân thủ chuẩn mã PEP8.
- [x] Chạy lại toàn bộ pipeline để xác nhận không lỗi trên tập dữ liệu đầy đủ.
- [ ] Làm sạch các file không sử dụng để chuẩn bị cho quá trình nộp (Submission).
