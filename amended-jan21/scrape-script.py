import pdfquery
from pdfquery.cache import FileCache
import csv

#Y-coordinates of lower left corners
zipcode_coords = [686, 551, 415, 279]
name_coords = [707, 571, 436, 300]
amount_coords = [718, 582, 446, 311]

zipcode_queries = ['LTTextLineHorizontal:in_bbox("67, ' + str(x) + ', 210, ' + str(x+15) + '")' for x in zipcode_coords]
amount_queries = ['LTTextLineHorizontal:in_bbox("520, ' + str(x) + ', 580, ' + str(x+15) + '")' for x in amount_coords]
name_queries = ['LTTextLineHorizontal:in_bbox("67, ' + str(x) + ', 210, ' + str(x+15) + '")' for x in name_coords]

queries = zip(name_queries, zipcode_queries, amount_queries)

files = [{'name':'filing1.pdf',
          'start': 3,
          'end': 1150},   #1150
         {'name':'filing2.pdf',
          'start': 0,
          'end': 1144}] #1144

with open('data.csv', 'w') as out:
    fieldnames = ['name', 'amount', 'zipcode']
    writer = csv.DictWriter(out, fieldnames=fieldnames)
    writer.writeheader()
    for file in files:
        pdf = pdfquery.PDFQuery(file['name'])
        for page in range(file['start'],file['end']):
            pdf.load(page)
            for query in queries:
                result = pdf.extract([
                    ('name', query[0], lambda x: x.text()),
                    ('zipcode', query[1], lambda x: x.text()[-5:]),
                    ('amount', query[2], lambda x: x.text())
                ])
                writer.writerow(result)

            #Clear caches to allow for garbage collection
            pdf._pages=[]
            pdf._pages_iter = None
            pdf._elements = []
            
            print 'Finished page {}'.format(page)






