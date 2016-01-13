import pdfquery
import csv

pdf = pdfquery.PDFQuery("filing.pdf")

zipcode_coords = [686, 551, 417, 282]
amount_coords = [717.758, 583.141, 448.551, 313.933]

zipcode_queries = ['LTTextLineHorizontal:in_bbox("67, ' + str(x) + ', 210, ' + str(x+15) + '")' for x in zipcode_coords]
amount_queries = ['LTTextLineHorizontal:in_bbox("520, ' + str(x) + ', 580, ' + str(x+15) + '")' for x in amount_coords]
queries = zip(zipcode_queries,amount_queries)

pages = range(13,253)
data = []
for page in pages:
    pdf.load(page)
    for query in queries:
        result = pdf.extract([
                ('zipcode', query[0], lambda x: x.text()[-5:]),
                ('amount', query[1], lambda x: x.text())
            ])
        data.append(result)

with open('data.csv', 'w') as file:
    fieldnames = ['amount', 'zipcode']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)




