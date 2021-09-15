#  В эту директорию загружается устав, загруженный пользователем


from pdf2image import convert_from_path

pages = convert_from_path('ustav.pdf', 500)
import os

ustav = ''
for i, page in enumerate(pages):
    page.save(f'docs/out{i}.jpg', 'JPEG')
    os.system(f'tesseract -l rus docs/out{i}.jpg save/output{i}')
    with open(f'output{i}.txt', 'r') as file:
        sentence = file.read()
        ustav += sentence

news = ''
with open(f'news.txt', 'r') as file:
    news = file.read()

#  Расчитываем синтаксический скор 'похожести' устава и деятельности по новостям и отзывам

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('bert-base-nli-mean-tokens')

sen_embedding = model.encode([news, ustav])

from sklearn.metrics.pairwise import cosine_similarity

result = cosine_similarity([news], [ustav])
print(result[0])
