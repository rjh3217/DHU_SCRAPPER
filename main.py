from flask import Flask, render_template, request
from scrapper import search_incruit
import csv

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html", title="대구한의대")

@app.route("/search")
def search():
   keyword = request.args.get("keyword")

   #실제 스크래핑
   #jobs_incruit = search_incruit(keyword, 1)

   #임시 csv 파일을 불러오는 부분
   with open("to_save.csv", "r", encoding="cp949") as file:
      csv_reader = csv.reader(file)

      jobs = []
      for row in csv_reader:
         job = {
            "compny_name": row[1],
            "title": row[2],
            "location": row[3],
            "link": row[4]
         }

         jobs.append(job)

   print(jobs[1:])

   return render_template("search.html", keyword=keyword,jobs=enumerate(jobs[1:]) )

app.run()