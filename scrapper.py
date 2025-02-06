import requests
from bs4 import BeautifulSoup

def search_incruit(keyword, page):
    jobs = []

    for i in range(page):

        page_no = i * 30
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page_no}"

        respons = requests.get(url)
        #print(respons.status_code)
        soup = BeautifulSoup(respons.text, "html.parser")

        
        lis = soup.find_all("li", class_="c_col")
        for li in lis:
            compny_name = li.find("a", class_="cpname").text
            title = li.select_one("div.cell_mid > div.cl_top").get_text(strip=True)
            link = li.select_one("div.cell_mid > div.cl_top").find("a").get("href")
            location = li.select_one("div.cell_mid > div.cl_md").find_all("span")[2].get_text(strip=True).replace(">", " ")

            job = {
                "compny_name": compny_name,
                "title": title,
                "link": link,
                "location": location

            }

            jobs.append(job)

        print(f"{i+1}번째 페이지 스크래핑을 완료 했습니다.")
    return jobs


