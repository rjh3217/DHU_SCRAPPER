from flask import Flask, render_template, request
from scrapper import search_incruit, search_saramin

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html", title="대구한의대")

@app.route("/search")
def search():
   keyword = request.args.get("keyword")
   
   # 실제 스크래핑 하는 부분
   jobs_incruit = search_incruit(keyword, 1)  # 인크루트에서 1페이지 크롤링
   jobs_saramin = search_saramin(keyword, 1)  # 사람인에서 1페이지 크롤링

   # 두 사이트의 결과 합치기
   jobs = jobs_incruit + jobs_saramin
   
   return render_template("search.html", keyword=keyword, jobs=enumerate(jobs))

if __name__ == "__main__":
   app.run(debug=True)