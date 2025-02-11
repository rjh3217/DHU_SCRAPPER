import requests
from bs4 import BeautifulSoup

# 공통 헤더 설정
HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

def fetch_job_data(url, selector, job_selector):
    """
    주어진 URL에서 HTML 데이터를 가져와서 직무 정보를 파싱하는 함수
    """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_item in soup.select(job_selector):
        job = {
            "company_name": job_item.select_one(selector["company_name"]).text.strip() if job_item.select_one(selector["company_name"]) else "정보 없음",
            "title": job_item.select_one(selector["title"]).get_text(strip=True),
            "location": job_item.select_one(selector["location"]).get_text(strip=True) if job_item.select_one(selector["location"]) else "위치 없음",
            "link": job_item.select_one(selector["link"]).get("href") if job_item.select_one(selector["link"]) else "#",
        }
        jobs.append(job)
    
    return jobs

def search_incruit(keyword, pages):
    """
    인크루트에서 직무 검색 결과를 스크래핑하는 함수
    """
    jobs = []

    for page in range(pages):
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page * 30}"
        selectors = {
            "company_name": "a.cpname",
            "title": "div.cell_mid > div.cl_top",
            "location": "div.cell_mid > div.cl_md span:nth-child(3)",
            "link": "div.cell_mid > div.cl_top a",
        }
        job_data = fetch_job_data(url, selectors, "li.c_col")
        jobs.extend(job_data)
        print(f"{page + 1}번째 페이지 스크래핑을 완료했습니다.")
    
    return jobs

def search_saramin(keyword, pages):
    """
    사람인에서 직무 검색 결과를 스크래핑하는 함수
    """
    jobs = []

    for page in range(pages):
        url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}&searchpage={page * 20}"
        selectors = {
            "company_name": "strong.corp_name",
            "title": "h2.job_tit a",
            "location": "div.job_condition span",
            "link": "h2.job_tit a",
        }
        job_data = fetch_job_data(url, selectors, "div.item_recruit")
        jobs.extend(job_data)
        print(f"{page + 1}번째 페이지 스크래핑을 완료했습니다.")
    
    return jobs
