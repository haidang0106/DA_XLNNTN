"""
Module cào nội dung bài báo từ URL.
Hỗ trợ các trang báo phổ biến: VNExpress, Dân Trí, Tuổi Trẻ,
Thanh Niên, VietnamNet, và fallback chung cho các trang khác.
"""

import requests
from bs4 import BeautifulSoup


# Timeout cho request (giây)
REQUEST_TIMEOUT = 10

# Headers giả lập trình duyệt để tránh bị chặn bot
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Cấu hình CSS selector cho từng trang báo
SITE_CONFIGS = {
    "vnexpress.net": {
        "title": "h1.title-detail",
        "content": "article.fck_detail p.Normal",
    },
    "dantri.com.vn": {
        "title": "h1.title-page",
        "content": "div.singular-content p",
    },
    "tuoitre.vn": {
        "title": "h1.detail-title",
        "content": "div.detail-content p",
    },
    "thanhnien.vn": {
        "title": "h1.detail-title",
        "content": "div.detail-content p",
    },
    "vietnamnet.vn": {
        "title": "h1.content-detail-title",
        "content": "div.maincontent p",
    },
}


def _get_site_key(url):
    """
    Xác định trang báo từ URL.
    Trả về key tương ứng trong SITE_CONFIGS hoặc None.
    """
    for site_key in SITE_CONFIGS:
        if site_key in url:
            return site_key
    return None


def _extract_with_config(soup, config):
    """
    Trích xuất tiêu đề và nội dung dựa trên CSS selector config.
    """
    title = ""
    title_tag = soup.select_one(config["title"])
    if title_tag:
        title = title_tag.get_text(strip=True)

    paragraphs = soup.select(config["content"])
    content = " ".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

    return title, content


def _extract_generic(soup):
    """
    Fallback: trích xuất nội dung từ các trang không nằm trong danh sách.
    Sử dụng heuristics chung.
    """
    # Tiêu đề: lấy từ thẻ h1 hoặc <title>
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(strip=True)
    elif soup.title:
        title = soup.title.get_text(strip=True)

    # Nội dung: lấy tất cả thẻ <p> trong <article>, nếu không có thì lấy chung
    article = soup.find("article")
    if article:
        paragraphs = article.find_all("p")
    else:
        # Loại bỏ các phần không liên quan
        for tag in soup.find_all(["nav", "footer", "header", "aside", "script", "style"]):
            tag.decompose()
        paragraphs = soup.find_all("p")

    content = " ".join(
        p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 20
    )

    return title, content


def scrape_article(url):
    """
    Cào nội dung bài báo từ URL.

    Args:
        url (str): URL bài báo cần cào.

    Returns:
        dict: {
            "title": str,       # Tiêu đề bài báo
            "content": str,     # Nội dung chính
            "url": str,         # URL gốc
            "error": str|None   # Thông báo lỗi (None nếu thành công)
        }

    Raises:
        Không raise exception. Mọi lỗi được trả về qua trường "error".
    """
    result = {"title": "", "content": "", "url": url, "error": None}

    # Validate URL cơ bản
    if not url or not url.startswith(("http://", "https://")):
        result["error"] = "URL không hợp lệ. URL phải bắt đầu bằng http:// hoặc https://"
        return result

    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        result["error"] = f"Timeout: Không thể kết nối tới {url} trong {REQUEST_TIMEOUT}s"
        return result
    except requests.exceptions.ConnectionError:
        result["error"] = f"Lỗi kết nối: Không thể truy cập {url}"
        return result
    except requests.exceptions.HTTPError as e:
        result["error"] = f"Lỗi HTTP {e.response.status_code}: {url}"
        return result
    except requests.exceptions.RequestException as e:
        result["error"] = f"Lỗi request: {str(e)}"
        return result

    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Chọn strategy trích xuất
    site_key = _get_site_key(url)
    if site_key:
        title, content = _extract_with_config(soup, SITE_CONFIGS[site_key])
    else:
        title, content = _extract_generic(soup)

    # Kiểm tra kết quả
    if not content:
        result["error"] = "Không trích xuất được nội dung từ trang này. Có thể không phải bài báo."
        return result

    result["title"] = title
    result["content"] = content
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python scraper.py <URL>")
        sys.exit(1)

    test_url = sys.argv[1]
    print(f"\nĐang cào nội dung từ: {test_url}")
    data = scrape_article(test_url)

    if data["error"]:
        print(f"LỖI: {data['error']}")
    else:
        print(f"Tiêu đề: {data['title']}")
        print(f"Nội dung ({len(data['content'])} ký tự): {data['content'][:300]}...")
