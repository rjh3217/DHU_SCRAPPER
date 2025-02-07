import csv

def save_to_csv(jobs):
    with open("to_save.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(
            ["No", "회사이름", "공고제목", "군무지역", "자세히보기,"]
        )

        for i, job in enumerate(jobs):
            csv_writer.writerow(
                [
                    i+1,
                job["compny_name"],
                job["title"],
                job["location"],
                job["link"]
                ]
            )