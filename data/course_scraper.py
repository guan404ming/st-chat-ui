import requests
from bs4 import BeautifulSoup
import json

# 設定目標 URL
BASE_URL = "https://nol.ntu.edu.tw/nol/coursesearch/"
SEARCH_URL = BASE_URL + "search_for_02_dpt.php?current_sem=113-2&dpt_sel=7000&dptname=7050&yearcode=0&selcode=-1&coursename=&teachername=&alltime=yes&allproced=yes&allsel=yes&page_cnt=150&Submit22=%E6%9F%A5%E8%A9%A2"

# 使用 session 提高效率
session = requests.Session()

# 爬取課程列表頁面
try:
    response = session.get(SEARCH_URL, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
except requests.exceptions.RequestException as e:
    print(f"❌ 無法獲取課程列表頁面: {e}")
    exit(1)

# 找到所有課程的連結
course_links = [
    BASE_URL + link["href"]
    for link in soup.find_all("a", href=True)
    if "print_table.php?course_id=" in link["href"]
]

# 爬取每門課程的詳細資訊
def fetch_course_details(url):
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 嘗試尋找課程資訊的表格
        tables = soup.find_all("table")
        if len(tables) < 3:
            print(f"⚠️ 無法解析課程資料（網址: {url}）")
            return None
        table = tables[2]  # 通常課程資料在第三個表格
        
        # 安全地提取欄位內容
        def get_text_safe(index):
            try:
                return table.find_all("td")[index].text.strip()
            except (IndexError, AttributeError):
                return "N/A"

        # 課程資料
        course_data = {
            "course_name": get_text_safe(1),
            "semester": get_text_safe(3),
            "target_department": get_text_safe(5),
            "instructor": get_text_safe(7),
            "course_id": get_text_safe(9),
            "course_code": get_text_safe(11),
            "class": get_text_safe(13),
            "credits": get_text_safe(15),
            "duration": get_text_safe(17),
            "mandatory_or_elective": get_text_safe(19),
            "schedule": get_text_safe(21),
            "location": get_text_safe(23),
            "remarks": get_text_safe(25),
            "course_intro_video": get_text_safe(27),
            "core_capabilities": get_text_safe(29),
            "course_description": get_text_safe(35),
            "course_objectives": get_text_safe(37),
            "course_requirements": get_text_safe(39),
            "student_workload": get_text_safe(41),
            "office_hours": get_text_safe(43),
            "designated_reading": get_text_safe(45),
            "reference_books": get_text_safe(47),
            "grading": get_text_safe(49),
            "course_outline": " ".join(tables[-1].stripped_strings) if tables else "N/A"
        }

        print(f"✅ 成功獲取課程資訊: [{course_data['course_id']}] {course_data['course_name']}")

        return course_data

    except requests.exceptions.RequestException as e:
        print(f"❌ 無法獲取課程詳情（網址: {url}）: {e}")
        return None

# 依次爬取所有課程
courses = []
for link in course_links:
    course_info = fetch_course_details(link)
    if course_info:
        courses.append(course_info)

# 轉換為 JSON 格式並輸出
if courses:
    with open("data/courses.json", "w", encoding="utf-8") as f:
        json.dump(courses, f, indent=4, ensure_ascii=False)

    print(f"✅ 成功獲取 {len(courses)} 門課程資料")
else:
    print("⚠️ 未找到任何課程資料")
